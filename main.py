import get_mars_data, rest_api, requests, time


def main():
    rest_api.main()
    time.sleep(10)
    get_mars_data.main()



def demo():
    sol_id = "833"
    response = requests.get(get_mars_data.BASE + sol_id)
    results = response.json()
    if response.status_code != 200:
        print(response.text)
        return []
    return results



if __name__ == '__main__':
    main()
    time.sleep(10)
    print(demo())
