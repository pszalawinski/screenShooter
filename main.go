package main

import (
	"bufio"
	"fmt"
	"image"
	"image/png"
	"os"
	"time"

	"github.com/kbinani/screenshot"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Println("Provide : ")

	scanner.Scan()

	var inputPath string = scanner.Text()

	for inputPath != "3" {
		if inputPath == "1" {
			captureDisplay(1)
		}
		if inputPath == "2" {
			captureDisplay(2)
		}
	}

}

func captureDisplay(i int) {

	bounds := screenshot.GetDisplayBounds(i)

	img, err := screenshot.CaptureRect(bounds)
	if err != nil {
		panic(err)
	}
	t := time.Now().Second()
	fileName := fmt.Sprintf("%d_time-%d.png", i, t)
	save(img, fileName)
}

func save(img *image.RGBA, filePath string) {
	file, err := os.Create(filePath)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	png.Encode(file, img)
}
