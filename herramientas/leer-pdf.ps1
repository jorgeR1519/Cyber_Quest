param([string]$Ruta)
$enc=[Text.Encoding]::GetEncoding(28591)
$raw=$enc.GetString([IO.File]::ReadAllBytes((Resolve-Path -LiteralPath $Ruta)))
$objects=@{}; $streams=@{}; $maps=@{}; $fonts=@{}
foreach($m in [regex]::Matches($raw,'(?s)(\d+) 0 obj(.*?)endobj')) {
 $id=$m.Groups[1].Value; $v=$m.Groups[2].Value; $objects[$id]=$v
 if($v -match '/FlateDecode' -and $v -notmatch '/Subtype\s*/Image') {
  $sm=[regex]::Match($v,'(?s)stream\r?\n(.*?)\r?\n?endstream')
  if($sm.Success){try {
   $b=$enc.GetBytes($sm.Groups[1].Value); $ms=[IO.MemoryStream]::new($b,2,($b.Length-6)); $ds=[IO.Compression.DeflateStream]::new($ms,[IO.Compression.CompressionMode]::Decompress); $out=[IO.MemoryStream]::new(); $ds.CopyTo($out); $streams[$id]=$enc.GetString($out.ToArray())
  }catch{}}
 }
}
foreach($id in $streams.Keys){$s=$streams[$id]; if($s -match 'begincmap'){
 $map=@{}; foreach($block in [regex]::Matches($s,'(?s)beginbfchar(.*?)endbfchar')){foreach($p in [regex]::Matches($block.Groups[1].Value,'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>')){$map[$p.Groups[1].Value.ToUpper()]=[char][Convert]::ToInt32($p.Groups[2].Value,16)}}; $maps[$id]=$map
}}
foreach($m in [regex]::Matches($raw,'/((?:FT|F)\d+)\s+(\d+) 0 R')){
 $obj=$objects[$m.Groups[2].Value]; $u=[regex]::Match($obj,'/ToUnicode\s+(\d+) 0 R'); if($u.Success){$fonts[$m.Groups[1].Value]=$maps[$u.Groups[1].Value]}
}
foreach($id in ($streams.Keys | Sort-Object {[int]$_})){
 $s=$streams[$id]; if($s -notmatch '\bBT\b'){continue}; "`n--- Contenido $id ---"
 $pieces=@(); foreach($bt in [regex]::Matches($s,'(?s)BT(.*?)ET')){
  $v=$bt.Groups[1].Value; $f=[regex]::Match($v,'/((?:FT|F)\d+)\s+[\d.]+\s+Tf'); $map=$fonts[$f.Groups[1].Value]
  $pos=[regex]::Match($v,'([-\d.]+)\s+([-\d.]+)\s+Tm'); $str=''
  foreach($h in [regex]::Matches($v,'<([0-9A-Fa-f]+)>')){ $hex=$h.Groups[1].Value; for($i=0;$i -lt $hex.Length;$i+=4){$key=$hex.Substring($i,[Math]::Min(4,$hex.Length-$i)).ToUpper(); if($map -and $map.ContainsKey($key)){$str+=$map[$key]}else{$str+='?'}} }
  foreach($lit in [regex]::Matches($v,'\(((?:\\.|[^()\\])*)\)')){ $str += [regex]::Replace($lit.Groups[1].Value,'\\([0-7]{1,3}|.)',{param($m) if($m.Groups[1].Value -match '^[0-7]+$'){[string][char][Convert]::ToInt32($m.Groups[1].Value,8)}else{$m.Groups[1].Value}}) }
  if($str){if($pos.Success){$y=[double]$pos.Groups[2].Value; $x=[double]$pos.Groups[1].Value}else{$y=$pieces.Count;$x=0}; $pieces += [pscustomobject]@{Y=$y; X=$x; Text=$str}}
 }
 $pieces | Group-Object Y | ForEach-Object {($_.Group | Sort-Object X | ForEach-Object {$_.Text}) -join ' '}
}
