from System import Int16
from ctypes import windll, Structure, c_ulong, byref

class POINT(Structure):
   _fields_ = [("x", c_ulong), ("y", c_ulong)]
   
if starting:
	pt = POINT()
	Joy_stat = False # данный флаг используется для включения передачи данных на джойстик
	vJoy_Enabled = False # данный флаг используется для временного отключения джойстика
	vJoy_Key = Key.CapsLock # кнопка на клавиатуре включающая режим управления джойстика мышкой
	Freeview = False # кнопка на клавиатуре включающая режим управления джойстика мышкой
	vJoy[0].x = 0 # инициализация джойстика
	vJoy[0].y = 0
	mouse_x = 0  # координаты мыши
	mouse_y = 0
	screen_x = windll.user32.GetSystemMetrics(0) # размер экрана
	screen_y = windll.user32.GetSystemMetrics(1)
	preci = 100  # уточнитель задает точность измерений до сотых, используется, для сохранения дробной части в умножителе
	scale_V = 100 # на какой угол в % отклоняется реальный джойстик, если меньше 100, то джойстик не наклоняется до конца
	scale_R = 100 # % масштабирования осей реального джойстика на экран, если меньше 100% то джойстик будет отклонятся до упора раньше
	# Внимание - не стоит задавать близкие значения Scale_V и Scale_R, так как это приведет к взаимовлиянию настроек. Одно из значений в паре пусть будет 100.
	multipler_x = preci * 32768 / screen_x # умножитель определяет, насколько нужно увеличить значение положения курсора, чтобы джойстик корректно отклонялся от центра экрана
	multipler_y = preci * 32768 / screen_y
	y_enabled = True

# ----------------------------------- Основной код ----------------------------------- #  

screen_x = windll.user32.GetSystemMetrics(0) # реинициализация определения размера экрана, при запуске приложений, для совместимости
screen_y = windll.user32.GetSystemMetrics(1)
multipler_x = preci * 32768 / screen_x # умножитель определяет, насколько нужно увеличить значение положения курсора, чтобы джойстик корректно отклонялся от центра экрана
multipler_y = preci * 32768 / screen_y

Freeview = mouse.middleButton # or mouse.getButton(3) # кнопки на мышке для свободного обзора. mouse.middleButton .rightButton .leftButton - средняя, правая или левая кнопка мыши и т.п.
#Freeview = keyboard.getKeyDown(Key.V) # пример для кнопки на клавиатуре для свободного обзора

# Включение и отключение джойстика
if keyboard.getPressed(vJoy_Key):
	if Joy_stat: # при отключении джойстик встает в 0
		Joy_stat = False
		vJoy_Enabled = False
		vJoy[0].x = 0
		vJoy[0].y = 0
	else:
		Joy_stat = True
		vJoy_Enabled = True

if vJoy_Enabled:
	if Freeview: # деактивация/активация джойстика, если нажата средняя кнопка мыши
		Joy_stat = False
		vJoy[0].x = 0
		vJoy[0].y = 0
	if not Freeview and Joy_stat == False:
		Joy_stat = True
		windll.user32.SetCursorPos(screen_x / 2, screen_y / 2) # автоцентрирование мыши при выходе из режима обзора

if Joy_stat:
	windll.user32.GetCursorPos(byref(pt))
	if pt.x > 65536: mouse_x = 0 # добавлено, так как при выходе значения за пределы int, происходил вылет скрипта
	else: mouse_x = pt.x
	if pt.y > 65536: mouse_y = 0 # добавлено, так как при выходе значения за пределы int, происходил вылет скрипта
	else: mouse_y = pt.y
	if keyboard.getPressed(Key.RightBracket): scale_V = scale_V + 10 # переключение масштабирования
	if keyboard.getPressed(Key.LeftBracket): scale_V = scale_V - 10 # переключение масштабирования
	if keyboard.getPressed(Key.Backslash): y_enabled = not y_enabled # переключение работы вертикальной оси
	# положение джойстика определяется как положение мыши на экране - половина ширина экрана умноженная на увеличитель и разделенная на уточнитель
	vJoy[0].x = (mouse_x - (screen_x / 2)) * multipler_x / preci * scale_V / scale_R 
	if y_enabled: vJoy[0].y = (mouse_y - (screen_y / 2)) * multipler_y / preci * scale_V / scale_R
	# кнопки на джойстике
	if mouse.leftButton: vJoy[0].setButton(0, True)
	else: vJoy[0].setButton(0, False)
	if mouse.rightButton: vJoy[0].setButton(1, True)
	else: vJoy[0].setButton(1, False)
	if mouse.getButton(3): vJoy[0].setButton(2, True)
	else: vJoy[0].setButton(2, False)
	if mouse.getButton(4): vJoy[0].setButton(3, True) 
	else: vJoy[0].setButton(3, False)

#диагностические значения
diagnostics.watch(Joy_stat)
diagnostics.watch(vJoy[0].x)
diagnostics.watch(vJoy[0].y)
diagnostics.watch(screen_x)
diagnostics.watch(scale_V)
diagnostics.watch(mouse.deltaX)