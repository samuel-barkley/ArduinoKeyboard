; Check if discord is active. If it is, it will print out an emoji.
if WinActive("ahk_exe Discord.exe")
{
	Send :CunoFace:
	Send {Enter}
}
else 
{
	; Stuff to do if discord is not open.
}

; Check if a program is running. If it is, focus that program. If it is, focus that program.
if WinExist("Streamlabs OBS")
	WinActivate
else 
	Run C:\Program Files\Streamlabs OBS\Streamlabs OBS.exe
