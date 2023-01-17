designFile = "C:/Users/Public/Documents/Altium/Projects/Cellar_Watchdog/PDNAnalyzer_Output/Cellar Watchdog/odb.tgz"

powerNets = ["+3V3", "VDDA3V3", "VDDIO", "LEDLA", "LEDLK", "LEDRA", "LEDRK", "+1V8", "+3V", "VBUS", "VUSB_RAW", "V_USB", "VIN"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "load",
"power_pins": [ ("U3", "19"), ("U3", "43"), ("U3", "46"), ("U3", "1"), ("U3", "26"), ("U3", "37") ],
"ground_pins": [ ("U3", "49") ],
"current": 1.2,
"Rpin": 0.142857142857143,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("R22", "2") ],
"ground_pins": [ ("S2", "3"), ("S2", "4") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("VR4", "5") ],
"ground_pins": [ ("VR4", "2") ],
"current": 0.01,
"Rpin": 10,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("R28", "2") ],
"ground_pins": [ ("VR4", "2") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("U6", "3") ],
"ground_pins": [ ("U6", "1") ],
"current": 0.0003,
"Rpin": 333.333333333333,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("U6", "4") ],
"ground_pins": [ ("U6", "1") ],
"current": 0.2,
"Rpin": 0.5,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("R43", "2") ],
"ground_pins": [ ("U6", "1") ],
"resistance": 1E-09,
"Rpin": 4100,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("R44", "2") ],
"ground_pins": [ ("U6", "1") ],
"resistance": 1E-09,
"Rpin": 1100,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("R45", "2") ],
"ground_pins": [ ("U6", "1") ],
"resistance": 1E-09,
"Rpin": 1100,
}
,
{
"id": "9",
"type": "load",
"power_pins": [ ("U7", "3") ],
"ground_pins": [ ("U7", "4") ],
"current": 0.0505,
"Rpin": 1.98019801980198,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("R46", "2") ],
"ground_pins": [ ("U7", "4") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("R47", "2") ],
"ground_pins": [ ("U7", "4") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("R31", "2") ],
"ground_pins": [ ("U5", "33"), ("U5", "29"), ("U5", "28") ],
"resistance": 1E-09,
"Rpin": 7500,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("R32", "2") ],
"ground_pins": [ ("U5", "33"), ("U5", "29"), ("U5", "28") ],
"resistance": 1E-09,
"Rpin": 7500,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("R33", "2") ],
"ground_pins": [ ("U5", "33"), ("U5", "29"), ("U5", "28") ],
"resistance": 1E-09,
"Rpin": 7500,
}
,
{
"id": "15",
"type": "load",
"power_pins": [ ("R34", "2") ],
"ground_pins": [ ("U5", "33"), ("U5", "29"), ("U5", "28") ],
"resistance": 1E-09,
"Rpin": 7500,
}
,
{
"id": "16",
"type": "load",
"power_pins": [ ("R35", "2") ],
"ground_pins": [ ("U5", "33"), ("U5", "29"), ("U5", "28") ],
"resistance": 1E-09,
"Rpin": 24750,
}
,
{
"id": "17",
"type": "load",
"power_pins": [ ("R38", "1") ],
"ground_pins": [ ("R38", "2") ],
"resistance": 1E-09,
"Rpin": 135,
}
,
{
"id": "18",
"type": "load",
"power_pins": [ ("R39", "1") ],
"ground_pins": [ ("R39", "2") ],
"resistance": 1E-09,
"Rpin": 135,
}
,
{
"id": "19",
"type": "load",
"power_pins": [ ("U4", "8") ],
"ground_pins": [ ("U4", "4"), ("U4", "9") ],
"current": 0.03,
"Rpin": 4.44444444444444,
}
,
{
"id": "20",
"type": "load",
"power_pins": [ ("R24", "2") ],
"ground_pins": [ ("U4", "4"), ("U4", "9") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "21",
"type": "load",
"power_pins": [ ("R25", "2") ],
"ground_pins": [ ("U4", "4"), ("U4", "9") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "22",
"type": "load",
"power_pins": [ ("R26", "2") ],
"ground_pins": [ ("U4", "4"), ("U4", "9") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "23",
"type": "load",
"power_pins": [ ("DS1", "12") ],
"ground_pins": [ ("DS1", "11") ],
"current": 0.001,
"Rpin": 100,
}
,
{
"id": "24",
"type": "load",
"power_pins": [ ("DS1", "A") ],
"ground_pins": [ ("DS1", "K") ],
"current": 0.036,
"Rpin": 2.77777777777778,
}
,
{
"id": "25",
"type": "load",
"power_pins": [ ("R42", "2") ],
"ground_pins": [ ("DS1", "K"), ("DS1", "11") ],
"resistance": 1E-09,
"Rpin": 666.666666666667,
}
,
{
"id": "26",
"type": "source",
"power_pins": [ ("J1", "A4_B9"), ("J1", "B4_A9") ],
"ground_pins": [ ("J1", "A1_B12"), ("J1", "B1_A12") ],
"voltage": 5,
"Rpin": 0.04,
}
,
{
"id": "27",
"type": "load",
"power_pins": [ ("VR1", "5"), ("VR1", "7"), ("VR1", "8") ],
"ground_pins": [ ("VR1", "6"), ("VR1", "9") ],
"current": 0.0087,
"Rpin": 34.4827586206897,
}
,
{
"id": "28",
"type": "load",
"power_pins": [ ("VR2", "6"), ("VR2", "1") ],
"ground_pins": [ ("VR2", "5"), ("VR2", "4"), ("VR2", "2") ],
"current": 0.00027,
"Rpin": 740.740740740741,
}
,
{
"id": "29",
"type": "load",
"power_pins": [ ("VR3", "3"), ("VR3", "1") ],
"ground_pins": [ ("VR3", "2") ],
"current": 0.002,
"Rpin": 100,
}
]


voltage_regulators = [
{
"id": "30",
"type": "linear",

"in": [ ("VR1", "5"), ("VR1", "7"), ("VR1", "8") ],
"out": [ ("VR1", "1"), ("VR1", "2"), ("VR1", "3") ],
"ref": [ ("VR1", "6"), ("VR1", "9") ],

"v2": -1.38794,
"i1": 0.0087,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "31",
"type": "linear",

"in": [ ("VR2", "6"), ("VR2", "1") ],
"out": [ ("VR2", "3") ],
"ref": [ ("VR2", "5"), ("VR2", "4"), ("VR2", "2") ],

"v2": -2.9059,
"i1": 0.00027,
"Ro": 58.94,
"Rpin": 39.2933333333333,
}
,
{
"id": "32",
"type": "linear",

"in": [ ("VR3", "3"), ("VR3", "1") ],
"out": [ ("VR3", "5") ],
"ref": [ ("VR3", "2") ],

"v2": -1.69353,
"i1": 0.002,
"Ro": 0,
"Rpin": 0,
}
,
{
"id": "33",
"type": "linear",

"in": [ ("FB3", "2") ],
"out": [ ("FB3", "1") ],
"ref": [],

"v2": -0.00066,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "34",
"type": "linear",

"in": [ ("FB4", "2") ],
"out": [ ("FB4", "1") ],
"ref": [],

"v2": -0.00049032,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "35",
"type": "linear",

"in": [ ("U5", "17") ],
"out": [ ("J4", "9") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "36",
"type": "linear",

"in": [ ("J4", "9") ],
"out": [ ("J4", "10") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.5,
}
,
{
"id": "37",
"type": "linear",

"in": [ ("U5", "17") ],
"out": [ ("U5", "31") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "38",
"type": "linear",

"in": [ ("J4", "12") ],
"out": [ ("J4", "11") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.5,
}
,
{
"id": "39",
"type": "linear",

"in": [ ("FB1", "1") ],
"out": [ ("FB1", "2") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "40",
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
"id": "41",
"type": "linear",

"in": [ ("Q1", "3") ],
"out": [ ("Q1", "4") ],
"ref": [],

"v2": -0.03822,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.02135,
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
