designFile = "C:/Users/Public/Documents/Altium/Projects/Cellar_Watchdog/PDNAnalyzer_Output/Cellar Watchdog/odb.tgz"

powerNets = ["VBUS", "VUSB_RAW", "V_USB", "RED_A", "STAT_LED", "GRN_K", "VIN", "VCCIO", "TRXLED", "BATTSW", "V_BATT", "BATTLED", "+3V3", "VDDA3V3", "VDDIO"]

groundNets = ["GND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J1", "B4_A9"), ("J1", "A4_B9") ],
"ground_pins": [ ("J1", "B1_A12"), ("J1", "A1_B12") ],
"voltage": 5,
"Rpin": 0.05,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("U1", "2"), ("U1", "1") ],
"ground_pins": [ ("U1", "9"), ("U1", "6") ],
"current": 0.0015,
"Rpin": 133.333333333333,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("U2", "4") ],
"ground_pins": [ ("U2", "13"), ("U2", "5") ],
"current": 0.022,
"Rpin": 6.06060606060606,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("R7", "1") ],
"ground_pins": [ ("R7", "2") ],
"resistance": 1E-09,
"Rpin": 280,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("R9", "2") ],
"ground_pins": [ ("U2", "13"), ("U2", "5") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("R10", "2") ],
"ground_pins": [ ("U2", "13"), ("U2", "5") ],
"resistance": 1E-09,
"Rpin": 6666.66666666667,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("R8", "1") ],
"ground_pins": [ ("R8", "2") ],
"resistance": 1E-09,
"Rpin": 5000,
}
,
{
"id": "7",
"type": "source",
"power_pins": [ ("U2", "9"), ("U2", "3"), ("U2", "2") ],
"ground_pins": [ ("U2", "13"), ("U2", "5") ],
"voltage": 3.3,
"Rpin": 0,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("R12", "1") ],
"ground_pins": [ ("U2", "13"), ("U2", "5") ],
"resistance": 1E-09,
"Rpin": 180,
}
,
{
"id": "9",
"type": "source",
"power_pins": [ ("J2", "2") ],
"ground_pins": [ ("J2", "1"), ("J2", "MP1"), ("J2", "MP2") ],
"voltage": 3.7,
"Rpin": 0.015,
}
,
{
"id": "10",
"type": "load",
"power_pins": [ ("R5", "1") ],
"ground_pins": [ ("R5", "2") ],
"resistance": 1E-09,
"Rpin": 191.5,
}
,
{
"id": "11",
"type": "load",
"power_pins": [ ("U3", "37"), ("U3", "26"), ("U3", "1"), ("U3", "46"), ("U3", "43"), ("U3", "19") ],
"ground_pins": [ ("U3", "49") ],
"current": 1.2,
"Rpin": 0.142857142857143,
}
,
{
"id": "12",
"type": "load",
"power_pins": [ ("VR4", "5") ],
"ground_pins": [ ("VR4", "2") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "13",
"type": "load",
"power_pins": [ ("U6", "3") ],
"ground_pins": [ ("U6", "1") ],
"current": 0.0001,
"Rpin": 1000,
}
,
{
"id": "14",
"type": "load",
"power_pins": [ ("U6", "4") ],
"ground_pins": [ ("U6", "1") ],
"current": 0.2,
"Rpin": 0.5,
}
,
{
"id": "15",
"type": "load",
"power_pins": [ ("U7", "3") ],
"ground_pins": [ ("U7", "4") ],
"current": 0.0005,
"Rpin": 200,
}
,
{
"id": "16",
"type": "load",
"power_pins": [ ("U5", "3") ],
"ground_pins": [ ("U5", "28"), ("U5", "29"), ("U5", "33") ],
"current": 0.055,
"Rpin": 2.72727272727273,
}
,
{
"id": "17",
"type": "load",
"power_pins": [ ("U5", "17") ],
"ground_pins": [ ("U5", "28"), ("U5", "29"), ("U5", "33") ],
"current": 0.015,
"Rpin": 10,
}
,
{
"id": "18",
"type": "load",
"power_pins": [ ("VR1", "8"), ("VR1", "7"), ("VR1", "5") ],
"ground_pins": [ ("VR1", "9"), ("VR1", "6") ],
"current": 0.0001,
"Rpin": 3000,
}
]


voltage_regulators = [
{
"id": "19",
"type": "linear",

"in": [ ("VR1", "8"), ("VR1", "7"), ("VR1", "5") ],
"out": [ ("VR1", "3"), ("VR1", "2"), ("VR1", "1") ],
"ref": [ ("VR1", "9"), ("VR1", "6") ],

"v2": -1.22287,
"i1": 1E-09,
"Ro": 0.135,
"Rpin": 0.2025,
}
,
{
"id": "20",
"type": "linear",

"in": [ ("FB1", "1") ],
"out": [ ("FB1", "2") ],
"ref": [],

"v2": -0.02,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "21",
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
"id": "22",
"type": "linear",

"in": [ ("Q1", "3") ],
"out": [ ("R4", "1") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5000,
}
,
{
"id": "23",
"type": "linear",

"in": [ ("D3", "3") ],
"out": [ ("D3", "1"), ("D3", "4") ],
"ref": [],

"v2": -1.8,
"i1": 0,
"Ro": 1E-06,
"Rpin": 3.33333333333333,
}
,
{
"id": "24",
"type": "linear",

"in": [ ("D3", "1"), ("D3", "4") ],
"out": [ ("D3", "2") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 3.33333333333333,
}
,
{
"id": "25",
"type": "linear",

"in": [ ("Q1", "3") ],
"out": [ ("Q1", "4") ],
"ref": [],

"v2": -0.25,
"i1": 0,
"Ro": 1E-06,
"Rpin": 5E-07,
}
,
{
"id": "26",
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
"id": "27",
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
"id": "28",
"type": "linear",

"in": [ ("D4", "1") ],
"out": [ ("D4", "2") ],
"ref": [],

"v2": -2.1,
"i1": 0,
"Ro": 1E-06,
"Rpin": 2.5,
}
,
{
"id": "29",
"type": "linear",

"in": [ ("FB3", "2") ],
"out": [ ("FB3", "1") ],
"ref": [],

"v2": -0.06,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
}
,
{
"id": "30",
"type": "linear",

"in": [ ("FB4", "2") ],
"out": [ ("FB4", "1") ],
"ref": [],

"v2": -0.22,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.006,
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
