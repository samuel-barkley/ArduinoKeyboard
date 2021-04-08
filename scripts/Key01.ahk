; Check if discord is active. If it is, it will print out an emoji.
if WinActive("ahk_exe Discord.exe")
{
	Send :SeulgiSun:
	Send {Enter}
}
else 
{
	; Stuff to do if discord is not open.
	if WinExist("ahk_exe Firefox.exe")
	{
		WinActivate
	}
	else 
	{
		Run C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox
	}
}


