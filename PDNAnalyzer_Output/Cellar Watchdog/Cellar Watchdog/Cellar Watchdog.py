designFile = "C:/Users/Public/Documents/Altium/Projects/Cellar_Watchdog/PDNAnalyzer_Output/Cellar Watchdog/odb.tgz"

powerNets = ["VBUS", "VUSB_RAW", "MAINSW", "V_USB", "VIN", "VCCIO", "TRXLED", "RED_A", "STAT_LED", "GRN_K", "BATTSW", "V_BATT", "BATTLED", "+3V3", "VDDA3V3", "VDDIO", "LEDLA", "LEDRA", "+1V8", "+3V"]

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
"power_pins": [ ("U1", "1"), ("U1", "2") ],
"ground_pins": [ ("U1", "6"), ("U1", "9") ],
"current": 0.0015,
"Rpin": 133.333333333333,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("U2", "4") ],
"ground_pins": [ ("U2", "5"), ("U2", "13") ],
"current": 0.022,
"Rpin": 6.06060606060606,
}
,
{
"id": "3",
"type": "source",
"power_pins": [ ("U2", "3") ],
"ground_pins": [ ("U2", "5"), ("U2", "13") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("R12", "1") ],
"ground_pins": [ ("U2", "5"), ("U2", "13") ],
"resistance": 1E-09,
"Rpin": 180,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("R7", "1") ],
"ground_pins": [ ("R7", "2") ],
"resistance": 1E-09,
"Rpin": 280,
}
,
{
"id": "6",
"type": "source",
"power_pins": [ ("J2", "2") ],
"ground_pins": [ ("J2", "MP2"), ("J2", "MP1"), ("J2", "1") ],
"voltage": 3.7,
"Rpin": 0.03,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("R5", "1") ],
"ground_pins": [ ("R5", "2") ],
"resistance": 1E-09,
"Rpin": 191.5,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("U3", "19"), ("U3", "43"), ("U3", "46"), ("U3", "1"), ("U3", "26"), ("U3", "37") ],
"ground_pins": [ ("U3", "49") ],
"current": 1.2,
"Rpin": 0.142857142857143,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("VR4", "5") ],
"ground_pins": [ ("VR4", "2") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("U6", "3") ],
"ground_pins": [ ("U6", "1") ],
"current": 0.0003,
"Rpin": 333.333333333333,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("U6", "4") ],
"ground_pins": [ ("U6", "1") ],
"current": 0.2,
"Rpin": 0.5,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("U7", "3") ],
"ground_pins": [ ("U7", "4") ],
"current": 0.0005,
"Rpin": 200,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("U5", "3") ],
"ground_pins": [ ("U5", "33"), ("U5", "29"), ("U5", "28") ],
"current": 0.053,
"Rpin": 2.83018867924528,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("U5", "17") ],
"ground_pins": [ ("U5", "33"), ("U5", "29"), ("U5", "28") ],
"current": 0.014,
"Rpin": 10.7142857142857,
}
,
{
"id": "15",
"type": "load",
"power_pins": [ ("J4", "9") ],
"ground_pins": [ ("J4", "8") ],
"resistance": 1E-09,
"Rpin": 135,
}
,
{
"id": "16",
"type": "load",
"power_pins": [ ("J4", "12") ],
"ground_pins": [ ("J4", "8") ],
"resistance": 1E-09,
"Rpin": 135,
}
,
{
"id": "17",
"type": "load",
"power_pins": [ ("U4", "8") ],
"ground_pins": [ ("U4", "4"), ("U4", "9") ],
"current": 0.03,
"Rpin": 4.44444444444444,
}
,
{
"id": "18",
"type": "load",
"power_pins": [ ("DS1", "12") ],
"ground_pins": [ ("DS1", "11") ],
"current": 0.001,
"Rpin": 100,
}
,
{
"id": "19",
"type": "load",
"power_pins": [ ("DS1", "A") ],
"ground_pins": [ ("DS1", "K") ],
"current": 0.036,
"Rpin": 2.77777777777778,
}
,
{
"id": "20",
"type": "load",
"power_pins": [ ("VR1", "5"), ("VR1", "7"), ("VR1", "8") ],
"ground_pins": [ ("VR1", "6"), ("VR1", "9") ],
"current": 0.002,
"Rpin": 150,
}
,
{
"id": "21",
"type": "load",
"power_pins": [ ("VR2", "6"), ("VR2", "1") ],
"ground_pins": [ ("VR2", "5"), ("VR2", "4"), ("VR2", "2") ],
"current": 0.00027,
"Rpin": 740.740740740741,
}
,
{
"id": "22",
"type": "load",
"power_pins": [ ("VR3", "3"), ("VR3", "1") ],
"ground_pins": [ ("VR3", "2") ],
"current": 0.0001,
"Rpin": 2000,
}
]


voltage_regulators = [
{
"id": "23",
"type": "linear",

"in": [ ("VR1", "5"), ("VR1", "7"), ("VR1", "8") ],
"out": [ ("VR1", "1"), ("VR1", "2"), ("VR1", "3") ],
"ref": [ ("VR1", "6"), ("VR1", "9") ],

"v2": -1.16923333333333,
"i1": 0.002,
"Ro": 2.2,
"Rpin": 3.3,
}
,
{
"id": "24",
"type": "linear",

"in": [ ("VR2", "6"), ("VR2", "1") ],
"out": [ ("VR2", "3") ],
"ref": [ ("VR2", "5"), ("VR2", "4"), ("VR2", "2") ],

"v2": -2.686945,
"i1": 0.00027,
"Ro": 60,
"Rpin": 40,
}
,
{
"id": "25",
"type": "linear",

"in": [ ("VR3", "3"), ("VR3", "1") ],
"out": [ ("VR3", "5") ],
"ref": [ ("VR3", "2") ],

"v2": -1.47479,
"i1": 1.5E-05,
"Ro": 81,
"Rpin": 54,
}
,
{
"id": "26",
"type": "linear",

"in": [ ("FB1", "1") ],
"out": [ ("FB1", "2") ],
"ref": [],

"v2": -0.022,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "27",
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
"id": "28",
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
"id": "29",
"type": "linear",

"in": [ ("Q1", "3") ],
"out": [ ("Q1", "4") ],
"ref": [],

"v2": -0.075,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.02135,
}
,
{
"id": "30",
"type": "linear",

"in": [ ("D6", "1") ],
"out": [ ("D6", "2") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.5,
}
,
{
"id": "31",
"type": "linear",

"in": [ ("R4", "2") ],
"out": [ ("R4", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 280,
}
,
{
"id": "32",
"type": "linear",

"in": [ ("D3", "3") ],
"out": [ ("D3", "4"), ("D3", "1") ],
"ref": [],

"v2": -1.8,
"i1": 0,
"Ro": 1E-06,
"Rpin": 373.333333333333,
}
,
{
"id": "33",
"type": "linear",

"in": [ ("D3", "4"), ("D3", "1") ],
"out": [ ("D3", "2") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 373.333333333333,
}
,
{
"id": "34",
"type": "linear",

"in": [ ("S1", "2") ],
"out": [ ("S1", "2a") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.01,
}
,
{
"id": "35",
"type": "linear",

"in": [ ("D4", "1") ],
"out": [ ("D4", "2") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 191.5,
}
,
{
"id": "36",
"type": "linear",

"in": [ ("FB3", "2") ],
"out": [ ("FB3", "1") ],
"ref": [],

"v2": -0.022,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "37",
"type": "linear",

"in": [ ("FB4", "2") ],
"out": [ ("FB4", "1") ],
"ref": [],

"v2": -0.022,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "38",
"type": "linear",

"in": [ ("U5", "17") ],
"out": [ ("J4", "9") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 135,
}
,
{
"id": "39",
"type": "linear",

"in": [ ("U5", "17") ],
"out": [ ("J4", "12") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 135,
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
