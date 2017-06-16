class Tag:
	def __init__(self,link,title,content):
		self.link=link
		self.title=title
		self.content=content
	
	def get_html(self):
		return '''
		<tr>
             <td>&nbsp;</td>
             <td class="text2"><img src="../imagens/marcadores/seta.png" alt="seta" width="10" height="10" /></td>
             <td class="text2"><span class="conteudo_interno"><a href="downloads/resolucoes/consun/1978/{}">{}</a></span></td>
           </tr>
           <tr>
             <td>&nbsp;</td>
             <td class="text2">&nbsp;</td>
             <td class="conteudo_interno">{}</td>
             </tr>
		'''.format(self.link,self.title,self.content)
