def GetColorCode(ForegroundColorName=None, BackgroundColorName=None):
    color_codes = {
        'black': ('30', '40'), 'red': ('31', '41'), 'green': ('32', '42'),
        'yellow': ('33', '43'), 'blue': ('34', '44'), 'magenta': ('35', '45'),
        'cyan': ('36', '46'), 'white': ('37', '47'),
        'lightblack': ('90', '100'), 'lightred': ('91', '101'), 'lightgreen': ('92', '102'),
        'lightyellow': ('93', '103'), 'lightblue': ('94', '104'),
        'lightmagenta': ('95', '105'), 'lightcyan': ('96', '106'), 'lightwhite': ('97', '107'),
        'violet': ('35', '45'), 'purple': ('35', '45')
    }

    foreground_code = ""
    background_code = ""

    if ForegroundColorName and ForegroundColorName.lower() in color_codes:
        foreground_code = f"\033[{color_codes[ForegroundColorName.lower()][0]}m"
    elif ForegroundColorName:
        print(f"Invalid foreground color name. Please choose from: {', '.join(color_codes.keys())}.")

    if BackgroundColorName and BackgroundColorName.lower() in color_codes:
        background_code = f"\033[{color_codes[BackgroundColorName.lower()][1]}m"
    elif BackgroundColorName:
        print(f"Invalid background color name. Please choose from: {', '.join(color_codes.keys())}.")

    return foreground_code + background_code if foreground_code or background_code else "Invalid color names or missing colors."


Green = GetColorCode('red')
for i in range(100000):
    print(f'{Green}{20*i+1}',end=':\r')
print('\033[0m','Done')

print(GetBackgroundColorCode('LIGHTred')+'I am Data Scientist')