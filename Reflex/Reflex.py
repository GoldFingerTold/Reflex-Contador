import reflex as rx

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Decrement",
                bg="#FF0000",
                color="#FFF",
                border_radius="lg",
                on_click=State.decrement,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                bg="#009900",
                color="#FFF",
                border_radius="lg",
                on_click=State.increment,
            ),
        ),    spacing="1em",
    )

app = rx.App()
app.add_page(index)
app.compile()