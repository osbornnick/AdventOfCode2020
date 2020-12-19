$day = Read-Host "Enter day number"
$text = "with open('day$day.txt', 'r') as f: `n`tdata = f.read()"

if ( -not ( Test-Path -Path ./$day ) )
{
    New-Item -Path . -Name "$day" -ItemType "directory"
    New-Item -Path ./$day -Name "day$day.py" -ItemType "file" -Value $text
    New-Item -Path ./$day -Name "day$day.txt" -ItemType "file"
}
else 
{
    Write-Output "day ./$day already exists"
}