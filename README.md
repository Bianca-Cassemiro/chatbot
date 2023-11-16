# Chatbot

## Objetivo
O chatbot, desenvolvido como um nó no ROS (Sistema Operacional de Robôs), é projetado para interpretar comandos expressos em linguagem natural. Esses comandos capacitam os usuários a fornecer instruções de posicionamento para um robô de maneira intuitiva.

## Como utilizar o projeto
1) Clone este repositório
2) Vá para o workspace chatbot

3) Faça o build do projeto
   ```
   colcon build
   ```
5) Utilize este comando
   ```
    source install/local_setup.bash 
   ```
6) Execute o nó responsável pelo chatbot
   ```
     ros2 run chat_pacotinho chat
   ```
P.S. o script principal se chama "fala_comigo_bb.py"

## Video de demonstração 
[Screencast from 16-11-2023 17:45:43.webm](https://github.com/Bianca-Cassemiro/chatbot/assets/99203402/0994cbbd-aa60-419f-8dc7-51a573d1be80)
