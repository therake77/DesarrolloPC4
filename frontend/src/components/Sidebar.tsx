import { Avatar, Box, Flex, Separator, Stack, Text } from "@chakra-ui/react";
import type { NavItem, User } from "../types/layout";
import SidebarItem from "./SidebarItem";

interface SidebarProps {
  navItems: NavItem[];
  active: string;
  onNavigate: (label: string) => void;
  user: User;
}

export default function Sidebar({ navItems, active, onNavigate, user }: SidebarProps) {
  return (
    <Flex
      as="nav"
      flexDir="column"
      w="220px"
      bg="white"
      borderRightWidth="1px"
      borderColor="gray.200"
      py={4}
      px={3}
      justify="space-between"
      position="sticky"
      top="60px"
      h="calc(100vh - 60px)"
    >
      {/* Nav links */}
      <Stack gap={1}>
        {navItems.map((item) => (
          <SidebarItem
            key={item.label}
            item={item}
            active={active === item.label}
            onClick={onNavigate}
          />
        ))}
      </Stack>

      {/* User section at the bottom */}
      <Box>
        <Separator mb={3} />
        <Flex
          align="center"
          gap={3}
          px={3}
          py={2}
          borderRadius="md"
          cursor="pointer"
          _hover={{ bg: "gray.100" }}
        >
          <Avatar.Root size="sm">
            <Avatar.Fallback name={user.name} />
          </Avatar.Root>
          <Box>
            <Text fontSize="sm" fontWeight="semibold" color="gray.700" lineHeight="tight">
              {user.name}
            </Text>
            <Text fontSize="xs" color="gray.500">
              {user.email}
            </Text>
            <Text fontSize="xs" color="gray.500">
              Rol: {user.role === "SOLIDARIO" ? "Cuidador Solidario" : user.role === "PROFESIONAL" ? "Profesional" : user.role === "ESPECIALIZADO" ? "Especializado" : "No definido"}
            </Text>
          </Box>
        </Flex>
      </Box>
    </Flex>
  );
}
