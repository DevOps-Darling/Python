from viewstate import ViewState
base64_encoded_viewstate = 'fU1UIZBlBWtXv6C5n+WoBSFJABMR55bXiRQWIWbaP7x0vbAzWY44DbVyXfDv0bKElfXO/z4NbpITx2zvNWorgzVmOLU4T61TIaHMVgDI8Es='

vs = ViewState(base64_encoded_viewstate)
vs.decode()
('abdce',(True,1))