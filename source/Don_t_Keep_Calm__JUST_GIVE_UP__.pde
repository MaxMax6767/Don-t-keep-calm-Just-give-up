//Imports and definitions for CP5
import java.util.*;
import controlP5.*;
ControlP5 cp5;
DropdownList resolution, strafeLeft, strafeRight, Jump, strafeDown, launchMode;
Slider Music, Sound;

//Variables Decralation 
JSONObject settings;
String mode = "menu", MleftStr, MrightStr, MjumpStr, MdownStr;
PImage discord, music, Xmusic, sound, Xsound, back;
PFont Font;
Float Jsonr, SoundV, MusicV, Mleft, Mright, Mjump, Mdown;
int MleftInt, MrightInt, MjumpInt, MdownInt;

void setup() {
  //Create a window 900x600 using the screen's pixel density and placing a non-resizable window at the center of the screen 
  size(900, 600);
  pixelDensity(displayDensity());
  surface.setTitle("Don't keep calm, Just GIVE UP [Launching]");
  frameRate(60);    
  textAlign(CENTER);

  //Image Preloading
  discord = loadImage("Assets/Discord.png");
  music = loadImage("Assets/Music.png");
  Xmusic = loadImage("Assets/XMusic.png");
  sound = loadImage("Assets/Sound.png");
  Xsound = loadImage("Assets/Xsound.png");
  back = loadImage("Assets/back.png");

  //Settings File handeler
  settings = loadJSONObject("data/Jeu/settings.json");
  List res = Arrays.asList("864×576", "1080×720", "1152×768", "1350×900", "1620×1080", "2160×1440", "3240×2160"); //List of 3/2 Resolutions for the DropDown menu in settings. First one in the lise has index 0.0 and last one has index 6.0
  List UserEndKeys = Arrays.asList("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Space", "Arrow Left", "Arrow UP", "Arrow Down", "Arrow Right", "L Shift", "L Control");
  List BackEndKeys = Arrays.asList("K_a", "K_b", "K_c", "K_d", "K_e", "K_f", "K_g", "K_h", "K_i", "K_j", "K_k", "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r", "K_s", "K_t", "K_u", "K_v", "K_w", "K_x", "K_y", "K_z", "K_SPACE", "K_LEFT", "K_UP", "K_DOWN", "K_RIGHT", "K_LSHIFT", "K_LCTRL");
  List LaunchModes = Arrays.asList("Compiled Mode", "Not Compiled Mode");

  //ControlP5 library initialisation
  cp5 = new ControlP5(this);
  PFont p = createFont("Arial", 16); //Font used in the settings
  ControlFont font = new ControlFont(p);
  cp5.setColorForeground(#0fbff5);
  cp5.setColorBackground(#1f1f1f);
  cp5.setFont(font);
  cp5.setColorActive(#75f8ff);

  //Dropdown menu for resolutions and its settings using ControlP5 Library 
  resolution = cp5.addDropdownList("res")
    .addItems(res)
    .setPosition(25, 25)
    .setSize(200, 320)
    .setItemHeight(40)
    .setBarHeight(40)
    .setOpen(true)
    .setCaptionLabel("Resolution")
    ;

  //Dropdown menu for Left movement and its settings using ControlP5 Library 
  strafeLeft = cp5.addDropdownList("left")
    .addItems(UserEndKeys)
    .setPosition(250, 155)
    .setSize(148, 325)
    .setItemHeight(30)
    .setBarHeight(45)
    .setOpen(true)
    .setCaptionLabel("Strafe Left :")
    ;

  //Dropdown menu for Jump button and its settings using ControlP5 Library 
  Jump = cp5.addDropdownList("jump")
    .addItems(UserEndKeys)
    .setPosition(408, 155)
    .setSize(148, 325)
    .setItemHeight(30)
    .setBarHeight(45)
    .setOpen(true)
    .setCaptionLabel("Jump :")
    ;

  //Dropdown menu for Right movement and its settings using ControlP5 Library 
  strafeRight = cp5.addDropdownList("right")
    .addItems(UserEndKeys)
    .setPosition(566, 155)
    .setSize(148, 325)
    .setItemHeight(30)
    .setBarHeight(45)
    .setOpen(true)
    .setCaptionLabel("Strafe Right :")
    ;

  //Dropdown menu for down button and its settings using ControlP5 Library 
  strafeDown = cp5.addDropdownList("down")
    .addItems(UserEndKeys)
    .setPosition(724, 155)
    .setSize(148, 325)
    .setItemHeight(30)
    .setBarHeight(45)
    .setOpen(true)
    .setCaptionLabel("Move Down :\n")
    ;

  //Slider for sound volume
  Sound = cp5.addSlider("son")
    .setPosition(250, 25)
    .setSize(464, 40)
    .setRange(0, 100)
    .setValue(settings.getFloat("SoundsVolume"))
    .setCaptionLabel(" Sound Volume")
    ;

  //Slider for music volume
  Music = cp5.addSlider("mus")
    .setPosition(250, 90)
    .setSize(464, 40)
    .setRange(0, 100)
    .setValue(settings.getFloat("MusicVolume"))
    .setCaptionLabel(" Music Volume")
    ;
}

void draw() {
  List BackEndKeys = Arrays.asList("K_a", "K_b", "K_c", "K_d", "K_e", "K_f", "K_g", "K_h", "K_i", "K_j", "K_k", "K_l", "K_m", "K_n", "K_o", "K_p", "K_q", "K_r", "K_s", "K_t", "K_u", "K_v", "K_w", "K_x", "K_y", "K_z", "K_SPACE", "K_LEFT", "K_UP", "K_DOWN", "K_RIGHT");

  //On click release open the list (prevents the dropdown menu from closing themselves 
  resolution.onRelease(new CallbackListener() {
    public void controlEvent(CallbackEvent theEvent) {
      resolution.setOpen(true);
    }
  }
  );
  strafeLeft.onRelease(new CallbackListener() {
    public void controlEvent(CallbackEvent theEvent) {
      strafeLeft.setOpen(true);
    }
  }
  );
  strafeRight.onRelease(new CallbackListener() {
    public void controlEvent(CallbackEvent theEvent) {
      strafeRight.setOpen(true);
    }
  }
  );
  Jump.onRelease(new CallbackListener() {
    public void controlEvent(CallbackEvent theEvent) {
      Jump.setOpen(true);
    }
  }
  );
  strafeDown.onRelease(new CallbackListener() {
    public void controlEvent(CallbackEvent theEvent) {
      strafeDown.setOpen(true);
    }
  }
  );

  //Submenu selector
  if (mode == "menu") {
    background(#1a1a1c);
    surface.setTitle("Don't keep calm, Just GIVE UP [Main Menu]");

    //Hide the controlP5 integration in the main menu
    resolution.hide();
    Sound.hide();
    Music.hide();
    strafeLeft.hide();
    strafeRight.hide();
    Jump.hide();
    strafeDown.hide();

    //Play Button Drawing
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(100/3, 100/3, 800/3, 100, 10);
    fill(255);
    textSize(60);
    text("Start", 165, 100); 

    //Play Button click action
    if (mouseX >= 30 && mouseX <= 300 && mouseY >= 30 && mouseY <= 135) {
      if (mousePressed == true) {
        exec(sketchPath("data/Jeu/Jeu.exe"));
        delay(50);
        exit();
      }
    }

    //Settings button Drawing
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(100/3, 500/3, 800/3, 100, 10);
    fill(255);
    textSize(52);
    text("Settings", 165, 233);

    //Settings button click action
    if (mouseX >= 30 && mouseX <= 300 && mouseY >= 165 && mouseY <= 260) {
      if (mousePressed == true) {
        mode = "settings";
      }
    }

    //Credits button Drawing
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(100/3, 302, 800/3, 200/3, 10);
    fill(255);
    textSize(42);
    text("Website", 165, 353); 

    //Credits button click action
    if (mouseX >= 30 && mouseX <= 300 && mouseY >= 300 && mouseY <= 370) {
      if (mousePressed == true) {
        link("https://keep-calm.great-site.net/");
      }
    }

    //Exit button Drawing
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(100/3, 402, 800/3, 200/3, 10);
    fill(255);
    textSize(42);
    text("Exit", 165, 450); 

    //exit button click action
    if (mouseX >= 30 && mouseX <= 300 && mouseY >= 400 && mouseY <= 470) {
      if (mousePressed == true) {
        exit();
      }
    }

    //Title Drawing
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(1000/3, 100/3, 1600/3, 200, 10);
    fill(255);
    textSize(60);
    text("Don't Keep Calm", 600, 110); 
    text("Just Give Up !", 600, 190); 

    //Logo Placeholder (Temporary)
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(450, 800/3, 300, 300, 10);
    fill(255);
    text("Logo", 600, 420);

    //QuickToggle button (sounds)
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(100/3, 502, 200/3, 200/3, 10);
    fill(255);
    textSize(55);
    text("S", 67, 557); 

    //Quick Setting for sounds click action (Checks the Settings file and return the opposite Boolean value on click)
    if (mouseX >= 30 && mouseX <= 100 && mouseY >= 500 && mouseY <= 570) {
      if (mousePressed == true) {
        if (settings.getBoolean("SoundsVolumeMute") == false) {
          settings.setBoolean("SoundsVolumeMute", true);
          saveJSONObject(settings, "settings.json");
          println("sound on");
          delay(100);
        } else {
          settings.setBoolean("SoundsVolumeMute", false);
          saveJSONObject(settings, "settings.json");
          println("sound off");
          delay(100);
        }
      }
    }

    //QuickToggle button (music)
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(700/3, 502, 200/3, 200/3, 10);
    fill(255);
    text("M", 267, 557); 

    //Quick Setting for music click action (Checks the Settings file and return the opposite Boolean value on click)
    if (mouseX >= 230 && mouseX <= 300 && mouseY >= 500 && mouseY <= 570) {
      if (mousePressed == true) {
        if (settings.getBoolean("MusicVolumeMute") == false) {
          settings.setBoolean("MusicVolumeMute", true);
          saveJSONObject(settings, "settings.json");
          println("music off");
          delay(100);
        } else {
          settings.setBoolean("MusicVolumeMute", false);
          saveJSONObject(settings, "settings.json");
          println("music on");
          delay(100);
        }
      }
    }

    //Discord redirect
    image(discord, 118, 500, 96, 77);
    if (mouseX >= 130 && mouseX <= 200 && mouseY >= 500 && mouseY <= 570) {
      if (mousePressed == true) {
        link("https://discord.gg/xCPzHgBHsh");
      }
    }

    //Image updating for QuickSetting Sounds based on the config file
    if (settings.getBoolean("SoundsVolumeMute") == false) {
      fill(50, 50, 50);
      stroke(183, 255, 250);
      strokeWeight(5);
      rect(100/3, 502, 200/3, 200/3, 10);
      image(sound, 40, 510, 50, 50);
    } else {
      fill(50, 50, 50);
      stroke(183, 255, 250);
      strokeWeight(5);
      rect(100/3, 502, 200/3, 200/3, 10);
      image(Xsound, 40, 510, 50, 50);
    }

    //Image updating for QuickSetting Music based on the config file
    if (settings.getBoolean("MusicVolumeMute") == false) {
      fill(50, 50, 50);
      stroke(183, 255, 250);
      strokeWeight(5);
      rect(700/3, 502, 200/3, 200/3, 10);
      image(music, 240, 510, 50, 50);
    } else {
      fill(50, 50, 50);
      stroke(183, 255, 250);
      strokeWeight(5);
      rect(700/3, 502, 200/3, 200/3, 10);
      image(Xmusic, 240, 510, 50, 50);
    }
  }

  //Settings Submenu
  if (mode == "settings") {
    clear();
    background(#1a1a1c);
    surface.setTitle("Don't keep calm, Just GIVE UP [Settings]");

    //Show the COntrolP5 items used for settings
    resolution.show();
    Sound.show();
    Music.show();
    strafeLeft.show();
    strafeRight.show();
    Jump.show();
    strafeDown.show();

    //Back Button
    fill(50, 50, 50);
    stroke(183, 255, 250);
    strokeWeight(5);
    rect(800, 500, 70, 70, 10);
    image(back, 790, 500, 80, 70);

    //Variables for quick acces to reduce CPU load
    Jsonr = resolution.getValue();
    SoundV = Sound.getValue();
    MusicV = Music.getValue();
    Mleft = strafeLeft.getValue();
    Mright = strafeRight.getValue();
    Mjump = Jump.getValue();
    Mdown = strafeDown.getValue();

    //Converts the FLoat outputs of the CP5 Library to Int to use in order to use the "get()" function for saving the settings
    //ControlP5 uses lists to set the position in the dropdown Menu
    MleftInt = Math.round(Mleft);
    MrightInt = Math.round(Mright);
    MjumpInt = Math.round(Mjump);
    MdownInt = Math.round(Mdown);

    //Back button click (Saves the settings)
    if (mouseX >= 800 && mouseX <= 870 && mouseY >= 500 && mouseY <= 570) {
      if (mousePressed == true) {
        mode = "menu";

        //Save the Resolution according to the index of the list in the DropDown Menu
        if (Jsonr == 6.0) {
          settings.setInt("displayResWidth", 3240);
          settings.setInt("displayresHeight", 2160);
        } else if (Jsonr == 0.0) {
          settings.setInt("displayResWidth", 864);
          settings.setInt("displayresHeight", 576);
        } else if (Jsonr == 1.0) {
          settings.setInt("displayResWidth", 1080);
          settings.setInt("displayresHeight", 720);
        } else if (Jsonr == 2.0) {
          settings.setInt("displayResWidth", 1152);
          settings.setInt("displayresHeight", 768);
        } else if (Jsonr == 3.0) {
          settings.setInt("displayResWidth", 1350);
          settings.setInt("displayresHeight", 900);
        } else if (Jsonr == 4.0) {
          settings.setInt("displayResWidth", 1620);
          settings.setInt("displayresHeight", 1080);
        } else if (Jsonr == 5.0) {
          settings.setInt("displayResWidth", 2160);
          settings.setInt("displayresHeight", 1440);
        }

        //If sounds are different from the settings file, it will save them (saves CPU usage)
        if (SoundV != settings.getFloat("SoundsVolume")) {
          settings.setFloat("SoundsVolume", SoundV);
        }
        if (MusicV != settings.getFloat("MusicVolume")) {
          settings.setFloat("MusicVolume", MusicV);
        }         
        if (BackEndKeys.get(MleftInt) != settings.getString("movementStrafeLeft")) {
          MleftStr = BackEndKeys.get(MleftInt).toString();
          settings.setString("movementStrafeLeft", MleftStr);
        }  
        if (BackEndKeys.get(MrightInt) != settings.getString("movementStrafeRight")) {
          MrightStr = BackEndKeys.get(MrightInt).toString();
          settings.setString("movementStrafeRight", MrightStr);
        }  
        if (BackEndKeys.get(MjumpInt) != settings.getString("movementJump")) {
          MjumpStr = BackEndKeys.get(MjumpInt).toString();
          settings.setString("movementJump", MjumpStr);
        }  
        if (BackEndKeys.get(MdownInt) != settings.getString("movementDown")) {
          MdownStr = BackEndKeys.get(MdownInt).toString();
          settings.setString("movementDown", MdownStr);
        } 

        //Developpement Tests
        println("Resolution : ", settings.getInt("displayResWidth"), "x", settings.getInt("displayresHeight"));
        println("Volume Sons : ", SoundV, "%");
        println("Volume Musique : ", MusicV, "%");
        println("Mouvement Gauche : ", MleftStr);
        println("Mouvement Jump : ", MrightStr);
        println("Mouvement Droite : ", MjumpStr);
        println("Mouvement bas : ", MdownStr);

        saveJSONObject(settings, "settings.json");
      }
    }
  }
};
