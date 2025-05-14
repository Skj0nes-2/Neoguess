install:
	@echo "Installing..."
	wget https://github.com/Skj0nes-2/Neoguess/releases/download/1.5.0/neoguess
	mv ./neoguess /usr/local/bin
	echo "alias neoguess='python /usr/local/bin/neoguess \"@#\"'" >> ~/.bashrc
	alias neoguess='python /usr/local/bin/neoguess "@#"'