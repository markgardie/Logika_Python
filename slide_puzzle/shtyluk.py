def check_for_quit():
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            terminate()