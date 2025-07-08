# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('variables.csv', '.')],  # Incluye el archivo CSV
    hiddenimports=[
        'models',
        'models.LectorCSV',
        'models.Simulacion', 
        'models.Sistema',
        'models.Subsistema',
        'models.Cliente',
        'utils',
        'scipy',
        'scipy.stats',
        'numpy',
        'matplotlib',
        'matplotlib.pyplot',
        'tabulate'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='simulacion',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
