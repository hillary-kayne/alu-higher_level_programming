elf, value):
            """Set the rectangle's width."""
                    if type(value) is not int:
                                    raise TypeError("width must be an integer")
                                        elif value < 0:
                                                        raise ValueError("width must be >= 0")
                                                            else:
                                                                            self.__width = value

                                                                                @property
                                                                                    def height(self):
                                                                                                """Get the rectangle's height."""
                                                                                                        return self.__height

                                                                                                        @height.setter
                                                                                                            def height(self, value):
                                                                                                                        """Set the rectangle's height."""
                                                                                                                                if type(value) is not int:
                                                                                                                                                raise TypeError("height must be an integer")
                                                                                                                                                    elif value < 0:
                                                                                                                                                                    raise ValueError("height must be >= 0")
                                                                                                                                                                        else:
                                                                                                                                                                                        self.__height = value
