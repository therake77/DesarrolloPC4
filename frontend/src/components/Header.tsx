import { Avatar, Flex, Heading, Icon } from "@chakra-ui/react";
import { LuBell } from "react-icons/lu";
import type { User } from "../types/layout";

interface HeaderProps {
  user: User;
}

export default function Header({ user }: HeaderProps) {
  return (
    <Flex
      as="header"
      h="60px"
      px={6}
      align="center"
      justify="space-between"
      bg="white"
      borderBottomWidth="1px"
      borderColor="gray.200"
      position="sticky"
      top={0}
      zIndex={10}
    >
      <Heading size="md" color="blue.600" letterSpacing="tight">
        MyApp
      </Heading>

      <Flex align="center" gap={4}>
        <Icon as={LuBell} boxSize={5} color="gray.500" cursor="pointer" />
        <Avatar.Root size="sm" cursor="pointer">
          <Avatar.Fallback name={user.name} />
        </Avatar.Root>
      </Flex>
    </Flex>
  );
}
