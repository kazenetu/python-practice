# filesのpngファイルを改名してresultにコピーする

from pathlib import Path
import os
import shutil

# 現在のパスを取得する
base_path = Path('.').absolute()

# pngファイルのルートパスを設定する
file_root_path = base_path.joinpath('files')

# 出力対象のフォルダ作成
output_path = base_path.joinpath('result')
if output_path.exists() == False:
    output_path.mkdir()

for f in file_root_path.glob('**/*.png'):
    # 相対パスを取得
    relative_path = f.relative_to(file_root_path)

    # ファイル名を取得
    file_name = str(relative_path.stem)

    # ディレクトリ名を取得
    dir_name = str(relative_path.parent).replace(os.path.sep,'_')
    if dir_name == '.':
        dir_name = ''
    else:
        dir_name += '_'

    # リネーム名を設定
    rename_name = '{0}{1}.png'.format(dir_name, file_name)

    print('filepath: ', rename_name )

    # ファイルコピー
    shutil.copy(f,output_path.joinpath(rename_name))
