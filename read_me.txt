##################################################################################

DOCUMENTAÇÃO TIBIA BOT
André Kadomoto

##################################################################################

>> config goto.py
  \venv\lib\site-packages\goto.py
  line 54: return code.replace(co_code=codestring)
  line 175: return _make_code(code, buf.tobytes())



>>check_supply_vai:

  <código de verificação>
  Ex.: check_supply("great_mana_potion"), check_img("scripts/carlin_cult/teste"), check_ammo()
  
  <valor de verificação>
  Ex.: qualquer valor numérico para checks de supply e ammo e True para check de imagens
  Check de imagens funionam apenas para verificar imagens não localizadas
  Como no caso de você entender que o personagem está na hunt quando não é localizada uma imagem do templo
  
  <label goto>
  Ex.: hunt, voltar, vender_itens, inicio