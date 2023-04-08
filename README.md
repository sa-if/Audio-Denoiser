<h1 align="center">Audio Noise Reduction. ✌️👍</h1>


` This script is designed to reduce noise in an audio file using the pydub, noisereduce, numpy, and matplotlib libraries.🙂
`

## Prerequisites 🤖
Install the following libraries using `pip`:
- `pydub`
- `noisereduce`
- `numpy`
- `matplotlib`

## Usage 😉
- Place the input audio file (in `.mp3` format) in the same directory as the script.
- Change the filename in the following line of code to match the name of your input audio file:  `audio = AudioSegment.from_file("input.mp3")`
- Run the script using a Python interpreter.
- The output audio file (reduced noise) will be saved in `.mp3` format with the name output.mp3 in the same directory as the script.

## How it works 🤖
- The script uses the `pydub` library to load the input audio file.
- The audio is then converted to a `numpy` array using numpy.
- The `noisereduce` library is used to reduce noise in the audio signal.
- The original and reduced noise signals are plotted using `matplotlib` for comparison.
- The reduced noise signal is then converted back to an audio format using `pydub`.
- Finally, the reduced noise audio is saved to a file using the `pydub library`.

## Note 🔉
- ` The results may vary depending on the input audio file. The user can adjust the parameters in the reduce_noise function for better results.`

## License ✔
The project is licensed under Apache-2.0 license license. See the `license` file for details.

## Authors 👦🏻

- [@saifislam](https://www.github.com/sa-if)

## Used By 🧑‍🤝‍🧑

This project is used by the following individual:

- `Saif Islam`  
- `Saimoon Islam`


## Support 💁🏻‍♂️

For support, email `saifislam23122005@gmail.com` or join `facebook` community.(●'◡'●)







