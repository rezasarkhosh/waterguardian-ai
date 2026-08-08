from src.data.factory import LoaderFactory
from src.config.config import Config


def main():

    config = Config("config.yaml")
    dataset_path = config.dataset_path

    loader = LoaderFactory.create(dataset_path)

    dataframe = loader.load()

    print(dataframe.head())



if __name__ == "__main__":
    main()
