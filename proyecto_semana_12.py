temperaturas = [
    [   # lago agrio
        [   # Semana1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 56},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana2
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana3
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 48},
            {"day": "Sábado", "temp": 51},
            {"day": "Domingo", "temp": 25}
        ],
        [   # Semana4
            {"day": "Lunes", "temp": 45},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 54},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ]
    ],
    [   # quito
        [   # Semana1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana2
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana4
            {"day": "Lunes", "temp": 34},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 40}
        ]
    ],
    [   # cuenca
        [   # Semana1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 44},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 42}
        ],
        [   # Semana2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 43},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana4
            {"day": "Lunes", "temp": 48},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 49},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

for i in range(len(temperaturas)):
    for j in range(i):
        promedio =(temperaturas[i, :, j])
        print(f"El promedio de temperaturas para {[i]} en {[j]} es {promedio:}")