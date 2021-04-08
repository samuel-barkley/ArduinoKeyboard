; Check if discord is active. If it is, it will print out an emoji.
if WinActive("ahk_exe Discord.exe")
{
	Send :CheyChey:
	Send {Enter}
}
else 
{
	; Stuff to do if discord is not open.
}
