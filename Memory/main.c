#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct stage {
    int buttons[4];
    int prompt;
    int pressed;
    int index;
} Stage;


void populate_stages(Stage *stage, int array[5][5]) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 4; j++) {
            stage[i].buttons[j] = array[i][j];
        }
        stage[i].prompt = array[i][4];
    }
}

void print_stage(Stage *stage) {
    printf("buttons: ");
    for (int i = 0; i < 4; i++) {
        printf("%d ", stage->buttons[i]);
    }
    printf("\np: %d, n %d, i%d\n\n", stage->prompt, stage->pressed, stage->index);
}

int find_pos(int *A, int N, int key) {
    for (int i = 0; i < N; i++) {
        if (A[i] == key) {
            return i;
        }
    }
    return -1;
}

void stage_1(Stage *stages) {
    if (stages[0].prompt == 1 || stages[0].prompt == 2) {
        stages[0].pressed = stages[0].buttons[1];
        stages[0].index = 1;
    } else if (stages[0].prompt == 3) {
        stages[0].pressed = stages[0].buttons[2];
        stages[0].index = 2;
    } else if (stages[0].prompt == 4) {
        stages[0].pressed = stages[0].buttons[3];
        stages[0].index = 3;
    }
}

void stage_2(Stage *stages) {
    switch (stages[1].prompt)
    {
    case 1:
    case 4:
        stages[1].pressed = 4;
        stages[1].index = find_pos(stages[1].buttons, 4, 4);
        break;
    case 2:
        stages[1].pressed = stages[1].buttons[stages[0].index];
        stages[1].index = stages[0].index;
        break;
    case 3:
        stages[1].pressed = stages[1].buttons[0];
        stages[1].index = 0;
        break;
    default:
        break;
    }
}

void stage_3(Stage *stages) {
    switch (stages[2].prompt) 
    {
    case 1:
        stages[2].index = find_pos(stages[2].buttons, 4, stages[1].pressed);
        stages[2].pressed = stages[2].buttons[stages[2].index];
        break;
    case 2:
        stages[2].index = find_pos(stages[2].buttons, 4, stages[0].pressed);
        stages[2].pressed = stages[2].buttons[stages[2].index];
        break;
    case 3:
        stages[2].index = 2;
        stages[2].pressed = stages[2].buttons[2];
        break;
    case 4:
        stages[2].pressed = 4;
        stages[2].index = find_pos(stages[2].buttons, 4, 4);
        break;
    }
}

void stage_4(Stage *stages) {
    switch (stages[3].prompt)
    {
    case 1:
        stages[3].pressed = stages[3].buttons[stages[0].index];
        stages[3].index = stages[0].index;
        break;
    case 2:
        stages[3].index = 0;
        stages[3].pressed = stages[3].buttons[0];
        break;
    case 3:
    case 4:
        stages[3].pressed = stages[3].buttons[stages[1].index];
        stages[3].index = stages[0].index; 
        break;
    }
}

void stage_5(Stage *stages) {
    switch (stages[4].prompt)
    {
    case 1:
        stages[4].pressed = stages[4].buttons[stages[0].index];
        stages[4].index = stages[0].index; 
        break;
    case 2:
        stages[4].pressed = stages[4].buttons[stages[1].index];
        stages[4].index = stages[0].index; 
        break;
    case 3:
        stages[4].pressed = stages[4].buttons[stages[2].index];
        stages[4].index = stages[0].index; 
        break;
    case 4:
        stages[4].pressed = stages[4].buttons[stages[3].index];
        stages[4].index = stages[0].index;  
        break;   
    }
}

int main() {

    int input[5][5] = {{1,3,2,4,1},{3,1,2,4,3},{2,3,4,1,2},{2,1,4,3,1},{4,1,2,3,4}};

    Stage stages[4];

    populate_stages(stages, input);

    stage_1(stages);
    stage_2(stages);
    stage_3(stages);
    stage_4(stages);
    stage_5(stages);

    for (int i = 0; i < 5; i++) {
        printf("%d", stages[i].pressed);
    }
    printf("\n");
}