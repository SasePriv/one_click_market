import { Button } from "@nextui-org/button";
import { ThemeSwitcher } from "@/components/ThemeSwitcher";
import {Card, CardHeader, CardBody, CardFooter, Divider, Link, Image} from "@nextui-org/react";

export default function Home() {
  return (
    <div className="flex flex-center w-full justify-center content-center h-screen p-10">
      <Card className="max-w-[600px]">
        <CardHeader className="flex gap-3">
          <Image
            alt="nextui logo"
            height={40}
            radius="sm"
            src="https://avatars.githubusercontent.com/u/86160567?s=200&v=4"
            width={40}
          />
          <div className="flex flex-col">
            <p className="text-md">One Click Market</p>
            <p className="text-small text-default-500">Peewi</p>
          </div>
          
        </CardHeader>
        <Divider/>
        <CardBody>
          <p>Make beautiful websites regardless of your design experience.</p>
        </CardBody>
        <Divider/>
        <CardFooter>
          <Link
            isExternal
            showAnchorIcon
            href="https://github.com/nextui-org/nextui"
          >
            Visit source code on GitHub.
          </Link>
        </CardFooter>
      </Card>
      {/* <ThemeSwitcher /> */}
    </div>
  )
}
