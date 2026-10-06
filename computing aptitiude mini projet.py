#include <stdio.h>
#include <string.h>

struct Transaction {
    char id[10];
    char op;
    char data[20];
};

int main() {
    struct Transaction t[10];
    int n, i, j;

    printf("Enter number of transactions: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("\nTransaction %d\n", i + 1);

        printf("Enter ID: ");
        scanf("%s", t[i].id);

        printf("Enter Operation (R/W): ");
        scanf(" %c", &t[i].op);

        printf("Enter Data Item: ");
        scanf("%s", t[i].data);
    }

    printf("\n===== TRANSACTION LOG =====\n");

    for (i = 0; i < n; i++) {
        printf("%s\t%c\t%s\n",
               t[i].id, t[i].op, t[i].data);
    }

    printf("\n===== CONFLICT ANALYSIS =====\n");

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {

            if (strcmp(t[i].data, t[j].data) == 0 &&
                (t[i].op == 'W' || t[j].op == 'W')) {

                printf("Conflict: %s and %s on %s\n",
                       t[i].id, t[j].id, t[i].data);
            }
        }
    }

    return 0;
}