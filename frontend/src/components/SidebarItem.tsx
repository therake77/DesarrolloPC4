import { Flex, Icon, Text } from "@chakra-ui/react";
import type { NavItem } from "../types/layout";

interface SidebarItemProps {
  item: NavItem;
  active: boolean;
  onClick: (label: string) => void;
}

export default function SidebarItem({ item, active, onClick }: SidebarItemProps) {
  return (
    <Flex
      align="center"
      gap={3}
      px={3}
      py={2}
      borderRadius="md"
      cursor="pointer"
      fontWeight={active ? "semibold" : "normal"}
      bg={active ? "blue.50" : "transparent"}
      color={active ? "blue.600" : "gray.600"}
      _hover={{ bg: active ? "blue.50" : "gray.100", color: "gray.900" }}
      onClick={() => onClick(item.label)}
    >
      <Icon as={item.icon} boxSize={5} />
      <Text fontSize="sm">{item.label}</Text>
    </Flex>
  );
}
