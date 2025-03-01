import dtlpy as dl


class HelloWorld(dl.BaseServiceRunner):
    def hello_world(self, item: dl.Item):
        """
        A simple function that prints and returns item details
        :param item: dl.Item to process
        :return: processed item
        """
        print(f"Processing item: {item.name}")
        print(f"Item ID: {item.id}")

        # Add a simple metadata flag
        if "user" not in item.metadata: 
            item.metadata["user"] = {}
        item.metadata["user"]["processed"] = True
        item.update()
        return item
