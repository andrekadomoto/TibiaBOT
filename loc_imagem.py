import cv2
from ss_save.ss_save import ss

def loc_imagem(img,cod):

    #root = r'C:\Users\andre\OneDrive\Área de Trabalho\pyCode\TibiaBOT'
    #img = r'fome'
    ss(cod)
    method = cv2.TM_SQDIFF_NORMED

    small_image = cv2.imread(img +'.png')
    large_image = cv2.imread('ss_save/screenshot_'+cod+'.png')
    result = cv2.matchTemplate(small_image, large_image, method)
    #def init_try(tries=0):
    #    try:
    #        result = cv2.matchTemplate(small_image, large_image, method)
    #        return result
    #    except Exception:
    #        if tries < sys.getrecursionlimit()*10000000:
    #            return init_try(tries+1)
    #        else:
    #            print('exceed')

    #result=init_try()

    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    MPx,MPy = mnLoc

    trows,tcols = small_image.shape[:2]

    cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    #cv2.imshow('output',large_image)
    #cv2.waitKey(0)

    return mn #if mn <= 0.00001 then ok else nok

#loc_imagem('barra_mana/barra_mana_80')

