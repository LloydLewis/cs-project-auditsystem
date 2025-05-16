# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\lloyd\\Downloads\\cs-project-auditsystem-main\\manage.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('website/templates', 'website/templates'),
        ('main_page/templates', 'main_page/templates'),
        ('login_system/templates', 'login_system/templates'),
        ('static', 'static')
    ],
    hiddenimports=[],
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
    name='manage',
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
