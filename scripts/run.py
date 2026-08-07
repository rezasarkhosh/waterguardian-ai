from src.data.factory import LoaderFactory

def main():

    loader = LoaderFactory.create("data/raw/example.csv")

    dataframe = loader.load()

    print(dataframe.head())



if __name__ == "__main__":
    main()
