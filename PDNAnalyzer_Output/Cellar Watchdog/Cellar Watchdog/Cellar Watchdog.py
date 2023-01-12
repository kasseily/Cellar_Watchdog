designFile = "C:/Users/Public/Documents/Altium/Projects/Cellar_Watchdog/PDNAnalyzer_Output/Cellar Watchdog/odb.tgz"

powerNets = ["VBUS", "VUSB_RAW", "MAINSW", "V_USB", "LEDK", "VIN", "+3V3", "+1V8", "+3V"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "A4_B9"), ("J1", "B4_A9") ],
"ground_pins": [ ("J1", "A1_B12"), ("J1", "B1_A12") ],
"voltage": 5,
"Rpin": 0.05,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("R1", "2") ],
"ground_pins": [ ("R1", "1") ],
"resistance": 1E-09,
"Rpin": 135,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("U1", "1"), ("U1", "2") ],
"ground_pins": [ ("U1", "6"), ("U1", "9") ],
"current": 0.0015,
"Rpin": 133.333333333333,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("D1", "1"), ("D1", "10") ],
"ground_pins": [ ("D1", "3"), ("D1", "8") ],
"current": 0.0001,
"Rpin": 2000,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U2", "4") ],
"ground_pins": [ ("U2", "5"), ("U2", "13") ],
"current": 0.022,
"Rpin": 6.06060606060606,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("U3", "19"), ("U3", "43"), ("U3", "46"), ("U3", "1"), ("U3", "26"), ("U3", "37") ],
"ground_pins": [ ("U3", "49") ],
"current": 1.2,
"Rpin": 0.142857142857143,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("U4", "8") ],
"ground_pins": [ ("U4", "4"), ("U4", "9") ],
"current": 0.03,
"Rpin": 4.44444444444444,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("DS1", "12") ],
"ground_pins": [ ("DS1", "11") ],
"current": 0.001,
"Rpin": 100,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("DS1", "A") ],
"ground_pins": [ ("DS1", "K") ],
"current": 0.036,
"Rpin": 2.77777777777778,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("VR1", "5"), ("VR1", "7"), ("VR1", "8") ],
"ground_pins": [ ("VR1", "6"), ("VR1", "9") ],
"current": 0.0001,
"Rpin": 3000,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("VR2", "6"), ("VR2", "1") ],
"ground_pins": [ ("VR2", "5"), ("VR2", "4"), ("VR2", "2") ],
"current": 0.0001,
"Rpin": 2000,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("VR3", "3"), ("VR3", "1") ],
"ground_pins": [ ("VR3", "2") ],
"current": 0.0001,
"Rpin": 2000,
}
]


voltage_regulators = [
{
"id": "12",
"type": "linear",

"in": [ ("VR1", "5"), ("VR1", "7"), ("VR1", "8") ],
"out": [ ("VR1", "1"), ("VR1", "2"), ("VR1", "3") ],
"ref": [ ("VR1", "6"), ("VR1", "9") ],

"v2": 12671.9,
"i1": 1E-09,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "13",
"type": "linear",

"in": [ ("VR2", "6"), ("VR2", "1") ],
"out": [ ("VR2", "3") ],
"ref": [ ("VR2", "5"), ("VR2", "4"), ("VR2", "2") ],

"v2": 12670.3,
"i1": 2E-06,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "14",
"type": "linear",

"in": [ ("VR3", "3"), ("VR3", "1") ],
"out": [ ("VR3", "5") ],
"ref": [ ("VR3", "2") ],

"v2": 12671.5,
"i1": 2E-07,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "15",
"type": "linear",

"in": [ ("FB1", "1") ],
"out": [ ("FB1", "2") ],
"ref": [],

"v2": -0.09,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.03,
}
,
{
"id": "16",
"type": "linear",

"in": [ ("F1", "1") ],
"out": [ ("F1", "2") ],
"ref": [],

"v2": -0.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.0175,
}
,
{
"id": "17",
"type": "linear",

"in": [ ("S1", "1") ],
"out": [ ("S1", "1a") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.01,
}
,
{
"id": "18",
"type": "linear",

"in": [ ("S1", "A") ],
"out": [ ("S1", "K") ],
"ref": [],

"v2": -2,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5,
}
,
{
"id": "19",
"type": "linear",

"in": [ ("Q1", "3") ],
"out": [ ("Q1", "4") ],
"ref": [],

"v2": -0.065,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5000,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 4, 'Thickness': 2E-05},
        {'name': 'L1__SIG_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.4, 'Thickness': 0.00011684},
        {'name': 'L2__GND_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-2', 'DielectricConstant': 4.6, 'Thickness': 0.00116},
        {'name': 'L3__GND_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'SUBSTRATE-3', 'DielectricConstant': 4.4, 'Thickness': 0.00011684},
        {'name': 'L4__SIG_', 'Conductivity': 47000000, 'Thickness': 3.5E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 4, 'Thickness': 2E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
