"use client";

import { useTheme } from "next-themes";
import { useEffect, useState } from "react";
import { Switch } from "@nextui-org/react";
import { RiMoonClearFill } from "react-icons/ri";
import { MdSunny } from "react-icons/md";

export function ThemeSwitcher() {
  const [mounted, setMounted] = useState(false);
  const { theme, setTheme } = useTheme();

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  const onHandleChane = (value: boolean)  => {
    setTheme(value ? 'light' : 'dark')
  }

  return (
    <Switch
      defaultSelected={theme === 'light'}
      size='lg'
      color='success'
      startContent={<MdSunny />}
      endContent={<RiMoonClearFill />}
      onValueChange={onHandleChane}
    >
    </Switch>
  );
}
