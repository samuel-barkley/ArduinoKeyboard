; Check if discord is active. If it is, it will print out an emoji.
if WinActive("ahk_exe Discord.exe")
{
	Send :Shrek:
	Send {Enter}
}
else 
{
	; Stuff to do if discord is not open.
	if WinExist("ahk_exe Discord.exe")
	{
		WinActivate
	}
	else 
	{
		Run, C:\Users\samue\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord
	}
}
