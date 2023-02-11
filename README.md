<p dir="auto" data-sourcepos="2:1-2:82">##################################################################################</p>
<h1 dir="auto" data-sourcepos="4:1-5:15"><span style="color: #00ff00;"><strong>DOCUMENTA&Ccedil;&Atilde;O TIBIA BOT </strong></span></h1>
<h4 dir="auto" data-sourcepos="4:1-5:15"><strong>Andr&eacute; Kadomoto</strong></h4>
<p dir="auto" data-sourcepos="7:1-7:82">##################################################################################</p>
<p>BOT ainda em desenvolvimento.</p>
<p>N&atilde;o possui reconhecimento de todas as features do jogo.</p>
<p>&nbsp;</p>
<p dir="auto" data-sourcepos="12:1-12:82">##################################################################################</p>
<h2 dir="auto" data-sourcepos="14:1-14:12">Pr&eacute; Requisitos</h2>
<p dir="auto" data-sourcepos="16:1-16:82">##################################################################################</p>
<p dir="auto" data-sourcepos="16:1-16:82"><a href="https://www.python.org/downloads/release/python-388/">Python 3.8.8</a></p>
<p dir="auto" data-sourcepos="16:1-16:82"><a href="https://code.visualstudio.com/">Visual Studio</a></p>
<p dir="auto" data-sourcepos="16:1-16:82"><a href="https://www.youtube.com/watch?v=ctcDfKYrzOQ">Configurar Python no Visual Studio</a></p>
<p>&nbsp;</p>
<p dir="auto" data-sourcepos="12:1-12:82">##################################################################################</p>
<h2 dir="auto" data-sourcepos="14:1-14:12">Instala&ccedil;&atilde;o</h2>
<p dir="auto" data-sourcepos="16:1-16:82">##################################################################################</p>
<h4 dir="auto" data-sourcepos="18:1-19:74"><strong>1-) Rodar 1.config_venv Objetivo: </strong></h4>
<p dir="auto" style="padding-left: 40px;" data-sourcepos="18:1-19:74">Configurar todas as bibliotecas necess&aacute;rias para executar o BOT</p>
<h4 dir="auto" data-sourcepos="21:1-22:71"><strong>2-) Rodar 2.install_funcoes Objetivo: </strong></h4>
<p dir="auto" style="padding-left: 40px;" data-sourcepos="21:1-22:71">Transformar todos os recursos do BOT em arquivos execut&aacute;veis</p>
<h4 dir="auto" data-sourcepos="24:1-26:60"><strong>3-) Rodar 3.criar_atalho Objetivo: </strong></h4>
<p dir="auto" style="padding-left: 40px;" data-sourcepos="24:1-26:60">Criar atalho do BOT na sua &aacute;rea de trabalho. Voc&ecirc; tamb&eacute;m pode escolher o &iacute;cone:</p>
<ul>
<li style="list-style-type: none;">
<ul>
<li dir="auto" data-sourcepos="24:1-26:60">Ferumbras Hat;</li>
<li dir="auto" data-sourcepos="24:1-26:60">Tibia Old School;</li>
<li dir="auto" data-sourcepos="24:1-26:60">Excercise Sword; Fire Sword</li>
</ul>
</li>
</ul>
<p dir="auto" data-sourcepos="29:1-29:82">##################################################################################</p>
<h2 dir="auto" data-sourcepos="31:1-31:13">Observa&ccedil;&otilde;es</h2>
<p dir="auto" data-sourcepos="33:1-33:82">##################################################################################</p>
<p>Erro na vers&atilde;o da fun&ccedil;&atilde;o GoTo</p>
<p>Corre&ccedil;&atilde;o: alterar linha 54 e 175 da fun&ccedil;&atilde;o GoTo</p>
<p dir="auto" data-sourcepos="37:4-40:50">config goto.py \venv\lib\site-packages\goto.py</p>
<ul>
<li dir="auto" data-sourcepos="37:4-40:50">line 54: return code.replace(co_code=codestring)</li>
<li dir="auto" data-sourcepos="37:4-40:50">line 175: return _make_code(code, buf.tobytes())</li>
</ul>
<p dir="auto" data-sourcepos="37:4-40:50">&nbsp;</p>
<h4 dir="auto" data-sourcepos="33:1-33:82">Como funciona o check_supplycheck_supply_vai:</h4>
<p dir="auto" data-sourcepos="46:3-47:94">&lt;c&oacute;digo de verifica&ccedil;&atilde;o&gt; Ex.: check_supply("great_mana_potion"), check_img("scripts/carlin_cult/teste"), check_ammo()</p>
<p dir="auto" data-sourcepos="49:3-52:110">&lt;valor de verifica&ccedil;&atilde;o&gt; Ex.: qualquer valor num&eacute;rico para checks de supply e ammo e True para check de imagens Check de imagens funionam apenas para verificar imagens n&atilde;o localizadas Como no caso de voc&ecirc; entender que o personagem est&aacute; na hunt quando n&atilde;o &eacute; localizada uma imagem do templo</p>
<p>Ex.: hunt, voltar, vender_itens, inicio</p>
