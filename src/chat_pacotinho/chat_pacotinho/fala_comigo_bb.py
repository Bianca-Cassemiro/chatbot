import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re
    

class UserInput:
    def __init__(self, intentions, actions):
        self.intentions = intentions
        self.actions = actions

    def user_input(self, user_input):
        user_input = user_input.lower().strip()
        for intention, patterns in self.intentions.items():
            for key in patterns:
                match = re.match(key, user_input, re.IGNORECASE)
                if match:
                    resposta = self.actions[intention](match.group(1))
                    return resposta
        return "Tenta de novo sô"

class Chat(Node):
    def __init__(self, input_user):
        super().__init__('chat')
        self.input = input_user
        self.publisher_ = self.create_publisher(String, 'chat', 10)
        self.subscription = self.create_subscription(
            String,
            'chat',
            self.listener_callback,
            10)
        self.subscription  

        self.get_logger().info('Chat inicializado')

    def listener_callback(self, msg):
        resposta = self.input.user_input(msg.data)
        response_msg = String()
        response_msg.data = resposta
        self.publisher_.publish(response_msg)
        self.get_logger().info('Resposta: "%s"' % resposta)


def main(args=None):

    rclpy.init(args=args)

    intentions =  {
    "caminha_jovem": [
        r"Encaminhe-me (?:para|ao|à|aos|a|às)? (.+)",
        r"Leve-me at[eé] (?:o|a|os|as)? (.+)",
        r"Preciso ir (?:para|ao|à|aos|às|a)? (.+)",
        r"Dirija-se (?:ao|à|aos|às)? (.+)",
        r"Partir (?:para|ao|à|aos|às)? (.+)",
        r"Mudar-se para (?:o|a|os|as)? (.+)",
        r"Tomar o caminho (?:para|ao|à|a|aos|às)? (.+)",
        r"Quero ser levado (?:para|ao|à|a|aos|às)? (.+)",
        r"Quero ir (?:para|ao|à|aos|às|a)? (.+)",
        r"Me leve (?:a|à)? (.+)",
        r"V[áa] para (.+)",
        r"Desloque-se (?:para|ao|à|aos|às)? (.+)",
        r"Rumo (?:a|ao|à|aos|às)? (.+)",
        r"Por favor, me encaminhe (?:para|ao|à|a|aos|às)? (.+)",
        r"Leve-me at[eé] (?:o|a|os|as)? (.+)",
        r"Ir para (?:o|a|os|as)? (.+)",
        r"Quero navegar (?:para|ao|à|aos|às)? (.+)",
        r"V[áa] para (?:o|a|os|as)? (.+)",
        r"Pode me levar (?:para|ao|à|a|aos|às)? (.+)",
        r"Encaminhe-me (?:para|ao|à|aos|a|às)? (.+)",
    ],
}
    
    actions_dict = {
        "caminha_jovem": lambda x: f"Vou te levar para {x} meu jovem",
}
    command = input("Digite o seu comando: ")
    
    input_user = UserInput(intentions, actions_dict)
    resposta = input_user.user_input(command)
    print(resposta)

if __name__ == '__main__':
    main()