class Tag:
	def __init__(self,link,title,content,year):
		self.link=link
		self.title=title
		self.content=content
		self.year=year
	
	def get_html(self):
		return '''
		<tr>
             <td>&nbsp;</td>
             <td class="text2"><img src="../imagens/marcadores/seta.png" alt="seta" width="10" height="10" /></td>
             <td class="text2"><span class="conteudo_interno"><a href="downloads/resolucoes/consun/{}/{}">{}</a></span></td>
           </tr>
           <tr>
             <td>&nbsp;</td>
             <td class="text2">&nbsp;</td>
             <td class="conteudo_interno">{}</td>
             </tr>
		'''.format(self.year,self.link,self.title,self.content)
