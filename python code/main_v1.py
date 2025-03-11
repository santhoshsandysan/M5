import os
import sys
import io
import time
import json
import _thread
from M5 import *
from hardwareimages = {
    'Men': 'men3.png',
    'Machine': 'machine1.png',
    'Method': 'method.png',
    'Measurement': 'measurement.png',
    'Material': 'material1.png',
    'Others': 'mt.png',
}
menu_imagee': 'idle.png',
    'Performance': 'oee.png',
    led = True
timeout_time = 30
current_menu = 0
current_submenu = 0
current_subsubmenu = 0
rotaryLR = 0
rotaryID = 0
rotaryID_last = 0
label1 = None
imacopy_file(src_filename, dst_filename):
    try:
  pen(dst_filename, 'w') as dst_file:
            dsfrom {src_filename} to {dst_filename}.")
    excep  with open(filename, 'r') as file:
            colename}:")
        print(content)
        return cError reading file: {e}")
        return None
def u, in_subsubmenu
    current_menu = 0
    current_R = 0
    rotaryID = 0
    rotaryID_last = 0
    ibmenu_selected_flag = False
    filename = 'startuname, 'w').close()
    json_content = None  # Initput("Stage: ")
        
        if x == "Start":
                user_input = input("Json: ")
                if user_input.lower() == 'quit':
                 break
                if user_input:
   s
                        file.write(user_input + to file.")
            
            copy_file(filename, new_filename)
        elif x == "End":
             print("JSON content read:", json_content)
ue  # Continue the loop to ask for input again
    if json_content:
        try:
            # Load JSON data
            data = json.loads(json_content)
            
            # Map JSON data to global variables
            global menu_options, submenu_options, subsubmenu_options
            
            menu_options = data.get('menu_options', [_options', {})
            subsubmenu_options = data.get('subsubmenu_options', {})
            
           print("Submenu Options:", submenu_options)
            print("Subsubmenu Options:", subsubmen
            print(f"Error decoding JSON: {e}")
def update_menu():
    # """Update the menu display based on the current menu selection."""
    global current_menu, rotaryLR, label1, image0, in_submenhandle_subsubmenu()
    elif in_submenu:
        #   else:
        # Adjust menu index based on rota        if current_menu >= len(menu_options):
     - 1
        # Clear screen and update display ele selected menu option
        menu_name = menu_options[current_menu]
        if menu_name in menu_imge0.setImage("res/img/mt.png")
        if menu_nam,0xFFFFFF,0x000000,menu_name,1)
        else:
    0000000, 0x000000)
          label_print(32,80,1.5,0xFFFFFF,0x000000,menu_name,1)
def show_submenu(mven menu option."""
    global in_submenu, submenu_images, current_submenu, submenu_options, image0,urrent_submenu = 0
    in_subsubmenu = False  # En    image0.setVisible(False)
    # Update image and label text based on selected submenu option
    submenu_name = submenu_options[menu_name][current_      image1.setImage("res/img/" + submenu_images[, 0xFFFFFF, 0x000000, submenu_name,2)
def handle_submenu():
    """Handle the display and navigation_submenu,init, submenu_options, rotaryLR, label1,  menu_name = menu_options[current_menu]
    if in_
        handle_subsubmenu()
    else:
        # A        current_submenu += rotaryLR
        if current_submenu >= len(submenu_options[menu_name]):
 t_submenu < 0:
            current_submenu = len(st_submenu <0 and init:
            current_submenu = 0
        label1.setText("                                   ")
        screenclear()
        # Uubmenu_options[menu_name][current_submenu]
        if submenu_name in submenu_images:
            imname])
        else:
            image1.setImage(" 0xFFFFFF, 0x000000, submenu_name,2)
def handle_subsubmenu():
    """Handle the display and navigatirrent_subsubmenu, init,subsubmenu_options, rotaryLR, label1, submenu_options, current_submenu, in_suenu_options[current_menu]][current_submenu]
    # rent_subsubmenu < 0:
        current_subsubmenu = l1.setText("                                   ")
120, 1.5, 0xFFFFFF, 0x000000, submenu_name,2)
    
    if subsubmenu_options[submenu_name][current_subsubmenu] == "Scan":
        print("select for scaning")
    else:
        Widgets.fillScreen(0x000000)
        label_print(79, 120, 1.5, 0xFFFFFF, 0ubsubmenu],2)
        
def open_menu():
    """Open the current menu option and update display accordingly."""
    global menu_options, current_menu, enu_options, current_subsubmenu
    if in_subsubmenu:
        return_to_home()  # Return to the home    # Move to subsubmenu if available
        submenu_name = submenu_options[menu_options[current_meubsubmenu_options:
            in_subsubmenu = Trucreenclear()
            # image0.setVisible(False)
            label1.setText(subsubmenu_options[su         # No subsubmenu, handle as usual
        lse:
        if menu_options[current_menu] == 'Pers.Rectangle(17, 98, 206, 30, 0x0000000, 0x000000)
            print("Performance")
            Performancein = input("Performance:")
            
            while len(Performancein) <2:
             mancesplit = Performancein.split('-')
            # print(Performancesplit)
                label1 = Widgets.Label("A : "+Performancesplit[0], 60, 46, 1.5, 0x000000, 0xc76600, Widgets.FONTS.DejaVu24)
                label2 = Widgets.Label("T : "+Performancesplit[1], 60, 146, 1.5, 0x000000, 0xc76600,u_options[current_menu] == 'Operator':
            screenclear()
            image1.setImage("res/img/rfid1.png")
            rfid_scanner("OP")
     mage("res/img/rfid1.png")
            rfid_scanner("RC")        
        elif menu_options[current_me.localtime()))
            image0.setVisible(False':
            return_to_home()
        elif menu     show_submenu(menu_options[current_menu])
      image0.setVisible(False)
            label1.setText("                                   ")
def return_to_menu():
    """Return to the main menu from a submenu."""
    global in_submenu, submenu_selebmenu
    Speaker.tone(1500, 50)
    time.sleep(1.en(0x000000)
    in_submenu = False
    in_subsubmcurrent_menu = menu_options.index('Performance')
 et submenu index
    update_menu()
def return_to_hbmenu."""
    global in_subsubmenu, in_submenu, current_menu, current_subsubmenu,rotary_enabled
    Speaker.tone(1500, 50)
    time.sleep(1.5)
    Spe0)
    rotary_enabled = True
    in_subsubmenu = Frent_menu + 5
    current_subsubmenu = 0
    updatel1
    label1 = Widgets.Label("", 25, 80, 2, 0xffffff, 0x000000, Widgets.FONTS.DejaVu18)
    update_menu()
def rotary_check():
    """Check and handle rotary encoder input."""
    global rotaryID, rotaryID_last, rotaryLR, in_submenu, in_subsubmenu
    if not rotary_enabled:
        return  # Ignorery.get_rotary_value()
    if rotaryID != rotaryID_last:
        rotaryLR = 1 if rotaryID > rotaryID_u:
            handle_subsubmenu()
        elif in_submenu:
            handle_submenu()
        els"""Clear the screen."""
    global label1, image0,1.setText("")
    image0.setImage("res/img/mt.png"ut_flag, rotary_enabled
    read_data = None
    timeout_flag = False
    # Disable rotary input
   read
    _thread.start_new_thread(timeout_thread, ())  
    while read_data is None and not timeout_ations
    # Clear screen after scanning
    Widge      print(split_state[0])
        
        if steen(0x49ff42)
            label_print(79, 120, 1.5   print("".join(chr(i) for i in read_data))
     ", 79, 155)
        else:
            Widgets.filll("Please scan", 20, 60, 1.5, 0xffffff, 0xff0000, ts.Label("Correct ID", 20, 100, 1.5, 0xffffff, 0xf= Widgets.Image("res/img/Incorrect.png", 79, 148)
Widgets.FONTS.DejaVu24)
        image3 = Widgets.Iled = False
    print("RFID")
    time.sleep(timeout_time)  # Wait for 10 seconds
    timeout_flag =ead_from_rfid():
    global rfid, timeout_flag
   is_new_card_present() and rfid.read_card_uid():
            block = 8  # Block to read data
            default_key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0earray
            key = bytearray(default_key)
            
            # Authenticate using the de0, block, key, rfid._uid):
                # Creatbuffer = bytearray(16)  # Typical block size is 16lock, buffer)
                rfid.pcd_stop_crypto1()  # Stop encryption on the PCD
                if status == rfid.STATUS_OK:
                    r rfid.pcd_stop_crypto1()
                return Nont high CPU usage
def label_print(x,y,size,tx,bg,text,align):
    global label1
    label1.setVisibl tx, bg, Widgets.FONTS.DejaVu24)
    if align == 1:
        label1.setText(text)
        label1 = Widgets.Label("", 0, y, size, tx, bg, Widgets.FONTS. label_align(spstr[0],bg,tx,123)
        elif len(spstr) == 2:
          Widgets.fillScreen(0x000000   label_align(spstr[1],bg,tx,144)
        elif le00)
          label_align(spstr[0],bg,tx,33)
     dgets.Label(text, 80, y, size, tx, bg, Widgets.FONTS.DejaVu24)
def label_align(labelstring,bgcolor,txtcolor,y):
    global in_submenu, in_sub_submenu, 240, 47, bgcolor, bgcolor)
    rect0.setVisible(T0
    # print(x)
    if(x<15):
      if x <0:
    1 = Widgets.Label("", x ,y, 2, txtcolor, bgcolor, Widgets.FONTS.DejaVu12)
      label1.setText(labelejaVu18)
      label1.setText(labelstring)
def inpd,init, in_submenu, current_menu, current_submenu, rotaryLR = 0
        if in_subsubmenu:
            submenu_name = submenu_options[menu_options[current_menu]][current_submenu]
            if menu_opptions[submenu_name][current_subsubmenu] != "Back":
                print("Reason-" + subsubmenu_opt      return_to_home()
            elif subsubmenuk":
                print("Back clicked")
        "before:"+str(current_submenu))
                cue]) + 6
                # print("after:"+str(current_submenu))
                # current_subsubmenu rrent_subsubmenu = 0
                update_ui()
 nu_name)
            else:
                return_bmenu
        elif in_submenu:
            submenu_name = submenu_options[menu_options[current_menu]subsubmenu_options:
                in_subsubmenu = True
                current_subsubmenu = 0
    etVisible(False)
                label_print(79, 1bmenu_name][current_subsubmenu], 2)
            elthe home menu if no subsubmenu available
        emance":
        Widgets.fillScreen(0x000000)
     f, 0xc76600)
        rect1 = Widgets.Rectangle(17,Performance:")
        Performancein = input("Performance:")
        while len(Performancein) <2:
      if len(Performancein) > 2: 
          Performal1 = Widgets.Label("A : "+Performancesplit[0], 60,24)
          label2 = Widgets.Label("T : "+Performancesplit[1], 60, 146, 1.5, 0x000000, 0xc76600, WThread function to check for input."""
    global ()
        time.sleep(0.1)  # Adjust the sleep timy, rfid
    M5.begin()
    Widgets.fillScreen(0x00ge("res/img/mt.png", 63, 119)
    image1 = Widgets cb=btnA_wasPressed_event)
    # _thread.start_new_thread(input_thread, ())
    variable_init()
    , ())
    image0.setVisible(True)
    image0.setIm
    update_ui()
def loop():
    """Main loop to continuously update the device."""
    M5.update()
    if rotary_enabled:
        rotary_check()
    :
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import      except ImportError:
            print("Please