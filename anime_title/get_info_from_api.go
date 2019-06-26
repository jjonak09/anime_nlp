package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

type ShangriLaAnimeAPI struct {
	ID    int    `json:"id"`
	Title string `json:"title"`
}

func main() {
	url := "http://api.moemoe.tokyo/anime/v1/master/"
	years := []string{"2014", "2015", "2016", "2017", "2018", "2019"}
	for _, year := range years {
		// fmt.Println(year)
		res, err := http.Get(string(url + year))
		if err != nil {
			log.Fatal(err)
		}
		body, err := ioutil.ReadAll(res.Body)
		if err != nil {
			log.Fatal(err)
		}
		defer res.Body.Close()
		var apiresponse []ShangriLaAnimeAPI
		if err := json.Unmarshal(body, &apiresponse); err != nil {
			log.Fatal(err)
		}
		// fmt.Println(len(apiresponse))

		file, err := os.OpenFile("anime_info.txt", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		for i := 0; i < len(apiresponse); i++ {
			// fmt.Println(apiresponse[i].Title)
			fmt.Fprintln(file, apiresponse[i].Title)
		}
	}
}
