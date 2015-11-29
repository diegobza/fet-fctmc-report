#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
tree = ET.parse('mater_subgroups.xml')
root = tree.getroot()

for periodo in root:
	per_nome = periodo.attrib.get('name')[:-35]
	print per_nome
	for dia in periodo:
		print dia.attrib.get('name')
		for horario in dia:
			print horario.attrib.get('name')


