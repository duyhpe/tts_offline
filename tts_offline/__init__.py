from .engine import Engine
import weakref

_activeEngines = weakref.WeakValueDictionary()

def khoitao(driverName=None, debug=False):
    '''
    Cấu trúc tạo mới một TTS hoặc tái sử dụng TTS có sẵn với 
    tên Driver hiện tại.

    @Tham số driverName: Tên của platform đặc biệt được sử dụng. Nếu là
        None, thì sử dụng mặc định theo cài đặt của hệ thống.
    @Kiểu dữ liệu: str - Dạng chuỗi (String)
    @Tham số debug: Cho phép/cấm chế độ gỡ lỗi 
    @Kiểu dữ liệu debug: bool - Dạng logic ( có giá trị là True hoặc False)
    @Kết quả trả về: Engine instance
    @Kiểu quả quả trả về: L{engine.Engine}
    '''
    try:
        eng = _activeEngines[driverName]
    except KeyError:
        eng = Engine(driverName, debug)
        _activeEngines[driverName] = eng
    return eng


def speak(text):
    engine = khoitao()
    engine.say(text)
    engine.runAndWait()


