package main

import (
	"bufio"
	"fmt"
	"image"
	"image/png"

	"os"

	"github.com/kbinani/screenshot"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Provide : ")

	scanner.Scan()

	var inputPath string = scanner.Text()
	if inputPath == "1" {
		captureDisplay()
	}

}

func printerOne() {
	fmt.Println("kliknieto jeden")
}

func printerTwo() {
	fmt.Println("kliknieto dwa")
}

func captureDisplay() {
	var i int = 1

	bounds := screenshot.GetDisplayBounds(i)

	img, err := screenshot.CaptureRect(bounds)
	if err != nil {
		panic(err)
	}
	fileName := fmt.Sprintf("%d_%dx%d.png", i, bounds.Dx(), bounds.Dy())
	save(img, fileName)
	fmt.Printf("#%d : %v \"%s\"\n", i, bounds, fileName)
}

func save(img *image.RGBA, filePath string) {
	file, err := os.Create(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	png.Encode(file, img)
}
