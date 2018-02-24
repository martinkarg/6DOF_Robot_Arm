//Codigo guardado como archivo de python para contar con algunas palabras reservadas y colores

import controlP5.*;
import processing.serial.*;

IntList Data_Read = new IntList();

ControlP5 cp5;

Accordion accordion;

color c = color(0, 160, 100);
int state = 0;
int init = 0;

controlP5.Button ManualBtn;
controlP5.Button AutomaticoBtn;
controlP5.Button RegresarBtn;
controlP5.Button GuardarBtn;

controlP5.Slider m1;
controlP5.Slider m2;
controlP5.Slider m3;
controlP5.Slider m4;
controlP5.Slider m5;
controlP5.Slider m6;

boolean DEBUG = true;

//poner posiciones home
int Motor1 = 10;
int Motor2 = 20;
int Motor3 = 30;
int Motor4 = 40;
int Motor5 = 50;
int Motor6 = 60;

void setup(){
    size(900, 700);
    noStroke();
    smooth();
    
    cp5 = new ControlP5(this);
    
    // create a new button with name 'Manual'
    // b1 = cp5.addButton("b1")
    ManualBtn = cp5.addButton("Manual")
        .setValue(4)
        .setPosition(width/2-130,200)
        .setSize(300,40)
    ;
         
    AutomaticoBtn = cp5.addButton("Automatico")
        .setValue(4)
        .setPosition(width/2-130,260)
        .setSize(300,40)
    ;

    RegresarBtn = cp5.addButton("Regresar")
        .setValue(4)
        .setPosition(-350,height-80)
        .setSize(300,40)
    ;
     
    GuardarBtn = cp5.addButton("Guardar Valores")
        .setValue(4)
        .setPosition(-350,height-80)
        .setSize(300,40)
    ;
     
    m1 = cp5.addSlider("Motor1")
        //.setPosition(width/2-100,160)
        .setPosition(-350,160)
        .setSize(200,40)
        .setRange(0,180)
    ;
     
    m2 = cp5.addSlider("Motor2")
        //.setPosition(width/2-100,220)
        .setPosition(-350,160)
        .setSize(200,40)
        .setRange(0,180)
    ;
       
    m3 = cp5.addSlider("Motor3")
        //.setPosition(width/2-100,280)
        .setPosition(-350,160)
        .setSize(200,40)
        .setRange(0,180)
    ;
     
    m4 = cp5.addSlider("Motor4")
        //.setPosition(width/2-100,340)
        .setPosition(-350,160)
        .setSize(200,40)
        .setRange(0,180)
    ;
       
    m5 = cp5.addSlider("Motor5")
        //.setPosition(width/2-100,400)
        .setPosition(-350,160)
        .setSize(200,40)
        .setRange(0,180)
    ;
       
    m6 = cp5.addSlider("Motor6")
        //.setPosition(width/2-100,460)
        .setPosition(-350,160)
        .setSize(200,40)
        .setRange(0,180)
    ;
}

void flujoBtn(String btnString, int Width, int Height, boolean caso){
    textSize(70);
    text(btnString, Width, Height);

    if (caso != false) 
    {
        ManualBtn.setPosition(-500,260);
        AutomaticoBtn.setPosition(-500,360);
        RegresarBtn.setPosition(width-350,height-80);
    } 
    else 
    {
        ManualBtn.setPosition(width/2-130,200);
        AutomaticoBtn.setPosition(width/2-130,260);
        RegresarBtn.setPosition(-350,height-80);
        GuardarBtn.setPosition(-350,height-80);
        m1.setPosition(-350,160);
        m2.setPosition(-350,220);
        m3.setPosition(-350,280);
        m4.setPosition(-350,340);
        m5.setPosition(-350,400);
        m6.setPosition(-350,460);
    }
}

void draw(){
    background(0,160,100);
    fill(255,255,255);

    PFont pfont = createFont("Arial", 20, true);
    ControlFont font = new ControlFont(pfont, 241);

    cp5.getController("Manual")
        .getCaptionLabel()
        .setFont(font)
        .setSize(30)
        .toUpperCase(false)
    ;

    cp5.getController("Automatico")
        .getCaptionLabel()
        .setFont(font)
        .setSize(30)
        .toUpperCase(false)
    ;

    cp5.getController("Regresar")
        .getCaptionLabel()
        .setFont(font)
        .setSize(30)
        .toUpperCase(false)
    ;

    cp5.getController("Guardar Valores")
        .getCaptionLabel()
        .setFont(font)
        .setSize(30)
        .toUpperCase(false)
    ;

    if(init == 0) 
    { 
        state = 0;
    }

    if (state == 0) 
    {    
        flujoBtn("RobApp", width/2-120, 100, false);
    } 
    
    //Entrar al modo manual
    else if (state == 1) 
    {
        flujoBtn("Modo Manual", width/2-180, 100, true);
        GuardarBtn.setPosition(50,height-80);

        m1.setPosition(width/2-100,160);
        m2.setPosition(width/2-100,220);
        m3.setPosition(width/2-100,280);
        m4.setPosition(width/2-100,340);
        m5.setPosition(width/2-100,400);
        m6.setPosition(width/2-100,460);
        //Valores de los motores guardados en variables Motor1, ... , Motor6
    }
    else if (state == 2)
    { //Entrar al modo automático
        flujoBtn("Modo Automático", width/2-250, 100, true);
    }

    init = 1;
}

public void controlEvent(ControlEvent theEvent) {
    if(theEvent.getController().getName() == "Manual")
    {
        println("Modo Manual");
        state = 1;
    }
    else if(theEvent.getController().getName() == "Automatico")
    {
        println("Modo Automatico");
        // Arturo, te regresa una IntList y ya de aquí puedes usar
        // sendPos(Data_Read, Indice) para mandarlo al arduino cuando
        // se presione el boton correspondiente
        Data_Read = readFile("data.csv");
        state = 2;
    }
    else if(theEvent.getController().getName() == "Regresar")
    {
        println("Modo Regresar");
        state = 0;
    }
    //ENVIAR INFORMACION DEL MOTOR 1, ... , MOTOR 6 AL ARCHIVO DE TEXTO. 
    //martin
    else if(theEvent.getController().getName() == "Guardar Valores")
    { 
        println("Valor motor 1 = " + Motor1);
        println("Valor motor 2 = " + Motor2);
        println("Valor motor 3 = " + Motor3);
        println("Valor motor 4 = " + Motor4);
        println("Valor motor 5 = " + Motor5);
        println("Valor motor 6 = " + Motor6);
        IntList motors = new IntList();
        motors.append(Motor1);
        motors.append(Motor2);
        motors.append(Motor3);
        motors.append(Motor4);
        motors.append(Motor5);
        motors.append(Motor6);
        sendPos(motors,0);
        savePosition("data.csv");
        
    }
    //println("test " + theEvent.getController().getName());
}

// Funciona
public IntList readFile(String file){
    // Reading a CSV file into a table object
    Table table = loadTable(file, "header");
    // Gets number of movements & thetas
    int movements = table.getRowCount();
    int thetas = table.getColumnCount();
    // Stores the movements into a matrix
    IntList list = new IntList();
    for(int i = 1; i < movements; i++){
        for(int j = 1; j < thetas; j++)
        {
            // Append column i, row j, data to list as an int
            list.append(table.getInt(i,j));
        }
    }
    if (DEBUG)
        // Prints the table
        table.print();
        // Prints the list
        println(list);
    return list;
}

// Funciona
public IntList readPos(){
    String read_data;
    IntList positions = new IntList();
    // Request motor positions from Arduino
    //Arduino_Port.write("pos");
    // Check if data is available
    /*
    if ( Arduino_Port.available() > 0) 
    {
        read_data = Arduino_Port.readStringUntil('\n');         // read it and store it in val
        // Parse data into IntList
        String[] motors_int = split(read_data, ',');
        for(int i = 0; i < 6; i++){
            positions.append(int(motors_int[i]));
        }
    } 
    */
    return positions;
}

// Funciona
public String sendPos(IntList positions, int index){
    String new_position =   str(positions.get(index)) + ',' + str(positions.get(index + 1)) + ',' 
                            + str(positions.get(index + 2)) + ',' + str(positions.get(index + 3)) 
                            + ',' + str(positions.get(index + 4)) + ',' + str(positions.get(index + 5)) 
                            + "\n";
    //Arduino_Port.write(new_position);
    return new_position;
}

// Funciona
public boolean executeMotors()
{
    IntList motors = new IntList();
    motors.append(Motor1);
    motors.append(Motor2);
    motors.append(Motor3);
    motors.append(Motor4);
    motors.append(Motor5);
    motors.append(Motor6);
    sendPos(motors, 0);
    return true;
}

// Funciona
public boolean savePosition(String file){
    Table table = new Table();
    file = "data/" + file;
    boolean file_exists = true;
    if (!file_exists)
    {
        // Create Header
        for(int i = 1; i <= 6; i++){
            table.addColumn("O" + str(i));
        }

        // Create Row
        TableRow newRow = table.addRow();
        newRow.setInt("O1", Motor1);
        newRow.setInt("O2", Motor2);
        newRow.setInt("O3", Motor3);
        newRow.setInt("O4", Motor4);
        newRow.setInt("O5", Motor5);
        newRow.setInt("O6", Motor6);
    }
    else
    {
        table = loadTable(file, "header");

        // Create Row
        TableRow newRow = table.addRow();
        newRow.setInt("O1", Motor1);
        newRow.setInt("O2", Motor2);
        newRow.setInt("O3", Motor3);
        newRow.setInt("O4", Motor4);
        newRow.setInt("O5", Motor5);
        newRow.setInt("O6", Motor6);
    }
    saveTable(table, file);
    return true;
}