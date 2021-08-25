import tts_offline
Máy_tính = tts_offline.init() # Khởi tạo 1 đối tượng mới

""" Tốc độ đọc"""
Tốc_Độ_Đọc = Máy_tính.getProperty('rate')       # Lấy thông tin tốc độ đọc hiện tại
print (Tốc_Độ_Đọc)                              # Hiển thị tốc độ hiện tại ra Terminal
Máy_tính.setProperty('rate', 125)               # Thiết lập lại tốc độ đọc là 125
Máy_tính.say("Hello!")
Máy_tính.say('My current speaking rate is ' + str(Tốc_Độ_Đọc))
Máy_tính.runAndWait()
Máy_tính.stop()

"""Âm lượng"""
Âm_Lượng = Máy_tính.getProperty('volume')                       # Lấy thông tin Âm lượng hiện tại (min=0 vào max=1)
print (Âm_Lượng)                                                # Hiển thị mức âm lượng hiện tại ra Terminal
Máy_tính.setProperty('volume',1.0)                              # Đặt lại mức âm lượng là 1.0 ( Max)
Máy_tính.say('My current speaking volume is ' + str(Âm_Lượng))
Máy_tính.runAndWait()
Máy_tính.stop()
"""Giọng nói"""
Giọng_Nói = Máy_tính.getProperty('voices')                      # Lấy thông tin giọng nói được cài đặt trong máy
Máy_tính.setProperty('voice', Giọng_Nói[1].id)                  # Thay đổi giọng nói; Có thể với máy khác nhau sẽ cho ra kết quả khác nhau. Nên cần kiểm tra ID phù hợp
Máy_tính.say("Chọn ngôn ngữ Tiếng Việt")
Máy_tính.runAndWait()
Máy_tính.stop()

Máy_tính.say("Xin chào!")
Máy_tính.say('Tốc độ đọc của tôi là: ' + str(Tốc_Độ_Đọc))
Máy_tính.runAndWait()
Máy_tính.stop()


"""Lưu 1 file test.mp3"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
Máy_tính.save_to_file('Chúc ngủ ngon', 'test.mp3')
Máy_tính.runAndWait()