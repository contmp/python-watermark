# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['source/watermark.py'],
             pathex=['/Users/contmp/Repositories/world/python-watermark'],
             binaries=[],
             datas=[('source/watermarker/*', 'watermarker')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Watermark',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='assets/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Watermark')
app = BUNDLE(coll,
             name='Watermark.app',
             icon='assets/Icon.icns',
             bundle_identifier='com.asdfer.watermark',
             info_plist={
                  'NSPrincipalClass': 'NSApplication',
                  'NSAppleScriptEnabled': False,
                  'CFBundleDocumentTypes': [
                      {
                          'CFBundleTypeExtensions': ["png", "jpg", "jpeg"],
                          'CFBundleTypeName': 'Image',
                          'CFBundleTypeRole': 'Viewer',
                          }
                      ]
                  },
              )
