#-*- coding: UTF-8 -*-  

import os
import time
from PIL import Image
from pathlib import Path
import setting

def analyseImage(path):
    '''
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode 
    before processing all frames.
    '''
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results


def processImage(path,target_folder):
    '''
    Iterate the GIF, extracting each frame.
    '''
    
    mode = analyseImage(path)['mode']
    
    im = Image.open(path)

    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')
    
    try:
        while True:
            # print "saving %s (%s) frame %d, %s %s" % (path, mode, i, im.size, im.tile)
            
            '''
            If the GIF uses local colour tables, each frame will have its own palette.
            If not, we need to apply the global palette to the new frame.
            '''
            if not im.getpalette():
                im.putpalette(p)
            
            new_frame = Image.new('RGBA', im.size)
            
            '''
            Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
            If so, we need to construct the new frame by pasting it on top of the preceding frames.
            '''
            if mode == 'partial':
                new_frame.paste(last_frame)
            
            new_frame.paste(im, (0,0), im.convert('RGBA'))
            targetR = (''.join(os.path.basename(path.name).split('.')[:-1]), i)
            # targetR.insert(0,target_folder)
            # targetR
            new_frame.save(target_folder + '/' + '%s-%d.png' % targetR, 'PNG')

            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass


def gif_images(box, source_folder, target_folder):
    t = int(time.time())

    source_path = Path(source_folder)
#     all_images = []
    for f in source_path.iterdir():
        t += len(box)
        processImage(f,target_folder)


def cut_gif(box=setting.box, source_folder='dataset/gif', target_folder='dataset/gif-new'):
    gif_images(box, source_folder, target_folder)


def cut_gif_test(box=setting.box, source_folder='dataset/test-gif', target_folder='dataset/gif-test'):
    gif_images(box, source_folder, target_folder)


def main():
    # processImage('ZwHNE_1564738511758.gif')
    cut_gif()
    

if __name__ == "__main__":
    main()