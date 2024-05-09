import pygame
import sys
import random
import os
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Multiple Choice Quiz")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (139,121,94)
BROWN = (238,207,161)  # Diamond blueish color
GREY = (180,205,205)
RED = (224,255,255)
# File to store high scores
high_scores_file = 'highscores.txt'

# Define fonts
font = pygame.font.Font(None, int(SCREEN_HEIGHT / 20))
small_font = pygame.font.Font(None, int(SCREEN_HEIGHT / 30))

# Define questions, answers, and results
questions = [
    "Welk type gesteente ontstaat door de metamorfose van bestaande gesteenten?",
    "Uit welk type gesteente wordt kalksteen gevormd?",
    "Welk type gesteente ontstaat door het afzetten en verdichten van sedimenten?",
    "Wat is een voorbeeld van losse sedimentaire gesteenten?",
    "Uit welk type gesteente ontstaat steenkool?",
    "Welk type gesteente is een voorbeeld van magmatische gesteenten?",
    "Welk type metamorf gesteente ontstaat uit graniet?",
    "Welk type sedimentair gesteente wordt gevormd uit grind?",
    "Welk soort gesteente wordt geassocieerd met klei en wordt gebruikt voor de productie van steenkool?",
    "Welk gesteente is een voorbeeld van een uitvloeiingsgesteente?",
    "Welk gesteente wordt gevormd door de afzetting van zand?",
    "Welk type sedimentair gesteente ontstaat uit zoutafzettingen?",
    "Het landinwaarts verplaatsen van de kustlijn door stijging van het zeeniveau is wat?",
    "Welke processen vinden plaats tijdens vulkanisme?",
    "Wat is het resultaat van divergerende plaatbewegingen op de zeebodem?",
    "Wat zijn de gevolgen van subductie?",
    "Wat gebeurt er tijdens convergerende plaatbewegingen?",
    "Wat is het gevolg van erosie op het aardoppervlak?",
    "Hoe worden metamorfe gesteenten gevormd?",
    "Welk type plaatbeweging vindt plaats bij een transformbreuk?",
    "Wat veroorzaakt seismische golven?",
    "Wat zijn de bouwstenen van gesteenten?",
    "Bij welke plooiingsfase hoort het tijdperk Siluur?",
    "Hoeveel miljoen jaar geleden vond het tijdperk Siluur plaats?",
    "In welk tijdperk vond de Hercynische plooiing plaats?",
    "Hoeveel miljoen jaar geleden vond het tijdperk Carboon plaats?",
    "Welke plooiingsfase vond plaats tijdens het tijdperk Oligoceen?",
    "Hoeveel miljoen jaar geleden vond het tijdperk Oligoceen plaats?",
    "Bij een vulkaanuitbarsting stolt magma en kan eroderen. Welk type lava is dit?",
    "Wat is een direct gevolg van inwendige krachten op de aarde?",
    "Wat is een direct gevolg van uitwendige krachten op de aarde?",
    "Wat is een omschrijving van geologie?",
    "Wat wordt bedoeld met de wet van superpositie?",
    "Wat is een kenmerk van de Mid-Atlantische Rug (MAR)?",
    "Hoe ontstaat organisch sedimentatiemateriaal?",
    "Wat zijn metamorfe gesteenten?",
    "Wat is een voorbeeld van een vaste sediment?",
    "Wat is een voorbeeld van een chemisch sediment?",
    "Wat is een voorbeeld van een metamorf gesteente?",
]

answers = [
    [["Igneous", False], ["Metamorf", True], ["Sedimentair", False], ["Magma", False]],
    [["Graniet", False], ["Leisteen", False], ["Kwartsiet", False], ["Sedimentair", True]],
    [["Igneous", False], ["Metamorf", False], ["Sedimentair", True], ["Magma", False]],
    [["Basalt", False], ["Kwartsiet", False], ["Grind", True], ["Graniet", False]],
    [["Sedimentair", True], ["Magmatisch", False], ["Metamorf", False], ["Kristallijn", False]],
    [["Metamorf", False], ["Sedimentair", False], ["Magma", False], ["Igneous", True]],
    [["Gneis", True], ["Kwartsiet", False], ["Marmer", False], ["Obsidiaan", False]],
    [["Dretitisch", False], ["Krijt", False], ["Turf", False], ["Zout", False]],
    [["Leisteen", True], ["Porfier", False], ["Obsidiaan", False], ["Marmer", False]],
    [["Basalt", True], ["Gneis", False], ["Turf", False], ["Kwartsiet", False]],
    [["Porfier", False], ["Leisteen", False], ["Zandsteen", True], ["Kalksteen", False]],
    [["Dretitisch", False], ["Kwartsiet", False], ["Marmer", False], ["Zout", True]],
    [["Transgressie", True], ["Convergentie", False], ["Divergentie", False], ["Regressie", False]],
    [["Smelten", True], ["Verdamping", False], ["Vorming", False], ["Aardbevingen", False]],
    [["Vorming", True], ["Verhoging", False], ["Toename", False], ["Smelten", False]],
    [["Veranderingen", True], ["Vorming van", False], ["Vorming van", False], ["Uitdroging", False]],
    [["Platen bewegen", True], ["Platen bewegen", False], ["Platen glijden", False], ["Platen blijven", False]],
    [["Verwering", True], ["Vorming van", False], ["Afname van", False], ["Verplaatsing van", False]],
    [["Hitte en druk", True], ["Sedimentatie", False], ["Vulkanische", False], ["Chemische", False]],
    [["Transformeren", True], ["Divergentie", False], ["Convergentie", False], ["Scheuren", False]],
    [["Plaatbewegingen", True], ["Oceanische", False], ["Vulkaanuitbarstingen", False], ["Windpatronen", False]],
    [["Mineralen", True], ["Cellen", False], ["Watermoleculen", False], ["Luchtdeeltjes", False]],
    [["Caledonische", True], ["Hercynische", False], ["Alpiene", False], ["Folenisch", False]],
    [["440-420 mil", True], ["450-520 mil", False], ["350-300 mil", False], ["35-0 mil", False]],
    [["Carboon", True], ["Siluur", False], ["Oligoceen", False], ["Foliceen", False]],
    [["350-300 mil", True], ["480-520 mil", False], ["440-420 mil", False], ["35-0 mil", False]],
    [["Alpiene", True], ["Caledonische", False], ["Hercynische", False], ["Feronisch", False]],
    [["35-0 mil", True], ["480-520 mil", False], ["440-420 mil", False], ["350-300 mil", False]],
    [["Basaltisch", True], ["Graniet", False], ["Obsidiaan", False], ["Pumice", False]],
    [["Aardbevingen", False], ["Gebergtevorm", True], ["Vulkanisme", False], ["Erosie", False]],
    [["Transport van", False], ["Gesteente worden", True], ["Bij het einde", False], ["Gebergtevorming", False]],
    [["Structuur", True], ["Weer op aarde", False], ["Sterrenstelsels", False], ["Oceanografie", False]],
    [["Oudste onder", True], ["Alle lagen in", False], ["De jongste lagen", False], ["De lagen in", False]],
    [["Onderzeese", True], ["Onderzeese", False], ["Diepe trog", False], ["Geologische", False]],
    [["Chemische", False], ["Fysische", False], ["Vulkanische", False], ["Opeenhoping", True]],
    [["Gevormd door", True], ["Nieuw gevormde", False], ["Gevormd door", False], ["Gevormd door", False]],
    [["Klei/leem", True], ["Zandsteen", True], ["Kalksteen", True], ["Conglomeraat", False]],
    [["Zout", True], ["Dretitisch", False], ["Grind", False], ["Zand", False]],
    [["Gneis", True], ["Kwartsiet", True], ["Leisteen", True], ["Marmer", True]]
]

# Define rank thresholds and names
rank_thresholds = {
    0: "Brons",
    10: "Zilver",
    20: "Goud",
    28: "Platinum",
    33: "Diamant"
}


# Function to determine the player's rank based on their score
def determine_rank(score):
    sorted_thresholds = sorted(rank_thresholds.items(), key=lambda x: x[0])
    best_rank = "Bronze"
    for threshold, rank in sorted_thresholds:
        if score >= threshold:
            best_rank = rank
    return best_rank


# Test the determine_rank function
def test_determine_rank():
    test_scores = [1, 3, 5, 7, 9]
    expected_ranks = ["Brons", "Zilver", "Goud", "Platinum", "Diamant"]

    for score, expected_rank in zip(test_scores, expected_ranks):
        actual_rank = determine_rank(score)
        print(f"Score: {score}, Verwachte Rang: {expected_rank}, Werkelijke Rang: {actual_rank}")


test_determine_rank()


# Function to read the player's rank from a file
def read_rank_from_file(filename):
    if not os.path.exists(filename):
        return "Brons"
    with open(filename, 'r') as file:
        rank = file.readline().strip()
    return rank


rank_scores_file = 'rank_scores.txt'

# Function to write the rank to a file


# Define variables
current_question = 0
score = 0

# Shuffle answers for the first question
random.shuffle(answers[current_question])

# Define button dimensions
BUTTON_RADIUS = int(SCREEN_HEIGHT / 8)
BUTTON_GAP_X = int(SCREEN_WIDTH / 15)
BUTTON_GAP_Y = int(SCREEN_HEIGHT / 20)

# Define border properties
border_color = BLUE
border_width = 4

# Define padding for the question and score borders
PADDING_X = 30
PADDING_Y = 20


class Button:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.rect = pygame.Rect(position[0] - BUTTON_RADIUS, position[1] - BUTTON_RADIUS, BUTTON_RADIUS * 2,
                                BUTTON_RADIUS * 2)
        self.clicked = False

    def draw(self):
        point_list = []
        for i in range(6):
            angle_rad = math.radians(60 * i + 30)
            x = self.position[0] + BUTTON_RADIUS * math.cos(angle_rad)
            y = self.position[1] + BUTTON_RADIUS * math.sin(angle_rad)
            point_list.append((x, y))
        pygame.draw.polygon(screen, BROWN, point_list)
        pygame.draw.polygon(screen, border_color, point_list, border_width)
        text_surface = small_font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.position)
        screen.blit(text_surface, text_rect)


# Function to read high scores from a text file
def read_high_scores(filename):
    if not os.path.exists(filename):
        return [0, 0, 0]
    with open(filename, 'r') as file:
        scores = [int(line.strip()) for line in file.readlines()]
    return scores


# Function to write high scores to a text file
def write_high_scores(filename, scores):
    with open(filename, 'w') as file:
        for score in scores:
            file.write(f"{score}\n")


# Function to update high scores with a new score
def update_high_scores(high_scores, new_score):
    if new_score in high_scores:
        return high_scores
    high_scores.append(new_score)
    high_scores.sort(reverse=True)

    high_scores = high_scores[:3]

    write_high_scores(high_scores_file, high_scores)

    return high_scores


image = pygame.image.load("backgroundmain.png")
# Function to draw the start page
def draw_start_page():
    background_image = pygame.image.load("background.jpg")

    screen.blit(background_image, (0, 0))

    start_text = font.render("Klik 's' om de quiz te starten", True, BLACK)
    start_text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    pygame.draw.rect(screen, GREY, start_text_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, start_text_rect)
    screen.blit(start_text, start_text_rect)

    high_score_info_text = small_font.render("Je kunt alleen verschillende topscores behalen.", True, BLACK)
    high_score_info_rect = high_score_info_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    pygame.draw.rect(screen, GREY, high_score_info_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, high_score_info_rect)
    screen.blit(high_score_info_text, high_score_info_rect)

    y_offset = 140
    high_scores_text = font.render("Hoogste Scores:", True, BLACK)
    high_scores_text_rect = high_scores_text.get_rect(topleft=(50, y_offset))

    high_scores_rect = pygame.Rect(high_scores_text_rect.topleft, (high_scores_text_rect.width + 40, 3 * 30 + 20))
    pygame.draw.rect(screen, GREY, high_scores_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, high_scores_rect)
    screen.blit(high_scores_text, high_scores_text_rect)

    high_scores = read_high_scores(high_scores_file)

    high_scores.sort(reverse=True)
    for idx, score in enumerate(high_scores[:3]):
        score_text = font.render(f"# {idx + 1}: {score}", True, BLACK)
        score_text_rect = score_text.get_rect(topleft=(50, y_offset + 30 * (idx + 1)))
        screen.blit(score_text, score_text_rect)

    pygame.display.flip()

# Function to draw the end screen
def draw_end_screen():
    screen.fill(WHITE)

    background_image = pygame.image.load("background.jpg")
    screen.blit(background_image, (0, 0))

    rank = determine_rank(score)

    rank_text = font.render("Rang: " + rank, True, BLACK)
    rank_rect = rank_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110))
    pygame.draw.rect(screen, GREY, rank_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, rank_rect)
    screen.blit(rank_text, rank_rect)

    final_score_text = font.render("Finale Score: " + str(score), True, BLACK)
    final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    pygame.draw.rect(screen, GREY, final_score_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, final_score_rect)
    screen.blit(final_score_text, final_score_rect)

    high_scores = read_high_scores(high_scores_file)  # Initialiseren van high_scores hier

    high_scores_text = font.render("Hoogste Scores:", True, BLACK)
    high_scores_rect = high_scores_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 70))
    pygame.draw.rect(screen, GREY, high_scores_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, high_scores_rect)
    screen.blit(high_scores_text, high_scores_rect)

    high_scores_text_rect = pygame.Rect(high_scores_rect.topleft, (high_scores_text.get_width(), 3 * 30 + 20))
    high_scores_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.draw.rect(screen, GREY, high_scores_text_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, high_scores_text_rect)

    y_offset = high_scores_text_rect.top + 20
    for i, high_score in enumerate(high_scores[:3]):
        score_text = small_font.render(f"# {i + 1}: {high_score}", True, BLACK)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, y_offset + i * 30))
        screen.blit(score_text, score_rect)

    restart_exit_text = font.render("Klik 'R' om te restarten   |   Klik 'Esc' om weg te gaan", True, BLACK)
    restart_exit_rect = restart_exit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
    pygame.draw.rect(screen, GREY, restart_exit_rect.inflate(20, 10))
    pygame.draw.rect(screen, RED, restart_exit_rect)
    screen.blit(restart_exit_text, restart_exit_rect)

    pygame.display.flip()

# Main start screen loop
start_screen_running = True

while start_screen_running:
    draw_start_page()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen_running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            start_screen_running = False

# Highscores initialiseren buiten de loop
high_scores = read_high_scores(high_scores_file)

# Main game loop
running = True
quiz_ended = False

while running:
    screen.fill(WHITE)

    screen.blit(image, (0, 0))

    if not quiz_ended:
        question_text = font.render(questions[current_question], True, BLACK)
        question_rect = question_text.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT / 10)))

        pygame.draw.rect(screen, BROWN, question_rect.inflate(PADDING_X, PADDING_Y))

        pygame.draw.rect(screen, border_color, question_rect.inflate(PADDING_X, PADDING_Y), border_width)

        screen.blit(question_text, question_rect)

        score_text = small_font.render("Score: " + str(score), True, BLACK)
        score_rect = score_text.get_rect(
            bottomleft=(int(SCREEN_WIDTH / 20), int(SCREEN_HEIGHT - SCREEN_HEIGHT / 20)))

        pygame.draw.rect(screen, BROWN, score_rect.inflate(PADDING_X, PADDING_Y))

        pygame.draw.rect(screen, border_color, score_rect.inflate(PADDING_X, PADDING_Y), border_width)

        screen.blit(score_text, score_rect)

        buttons = []
        for i, (answer, _) in enumerate(answers[current_question]):
            col = i % 2
            row = i // 2
            button_x = (SCREEN_WIDTH - BUTTON_RADIUS * 2 - BUTTON_GAP_X) // 2 + col * (
                    BUTTON_RADIUS * 2 + BUTTON_GAP_X)
            button_y = int(SCREEN_HEIGHT / 3) + row * (BUTTON_RADIUS * 2 + BUTTON_GAP_Y)
            button = Button(answer, (button_x, button_y))
            buttons.append(button)

        for button in buttons:
            button.draw()

    else:
        draw_end_screen()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if quiz_ended:
                if event.key == pygame.K_r:
                    current_question = 0
                    score = 0
                    quiz_ended = False

                    buttons.clear()
                    random.shuffle(answers[current_question])
                    for i, (answer, _) in enumerate(answers[current_question]):
                        col = i % 2
                        row = i // 2
                        button_x = (SCREEN_WIDTH - BUTTON_RADIUS * 2 - BUTTON_GAP_X) // 2 + col * (
                                BUTTON_RADIUS * 2 + BUTTON_GAP_X)
                        button_y = int(SCREEN_HEIGHT / 3) + row * (BUTTON_RADIUS * 2 + BUTTON_GAP_Y)
                        buttons.append(Button(answer, (button_x, button_y)))
                elif event.key == pygame.K_ESCAPE:
                    running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not quiz_ended:
            x, y = event.pos
            for button in buttons:
                if button.rect.collidepoint(x, y):
                    button.clicked = True
                    if answers[current_question][buttons.index(button)][1]:
                        score += 1
                    current_question += 1
                    if current_question < len(questions):
                        buttons.clear()
                        random.shuffle(answers[current_question])
                        for i, (answer, _) in enumerate(answers[current_question]):
                            col = i % 2
                            row = i // 2
                            button_x = (SCREEN_WIDTH - BUTTON_RADIUS * 2 - BUTTON_GAP_X) // 2 + col * (
                                    BUTTON_RADIUS * 2 + BUTTON_GAP_X)
                            button_y = int(SCREEN_HEIGHT / 3) + row * (BUTTON_RADIUS * 2 + BUTTON_GAP_Y)
                            buttons.append(Button(answer, (button_x, button_y)))
                        quiz_ended = False
                    else:
                        quiz_ended = True
                        # Update en schrijf de highscores naar het bestand
                        high_scores = update_high_scores(high_scores, score)
                        write_high_scores(high_scores_file, high_scores)


    # Controleer of een nieuwe highscore is behaald
    if quiz_ended and score > high_scores[0]:
        # Update en schrijf de highscores naar het bestand
        high_scores = update_high_scores(high_scores, score)
        write_high_scores(high_scores_file, high_scores)

screen.fill(WHITE)

draw_end_screen()

pygame.time.wait(3000)
pygame.quit()
sys.exit()